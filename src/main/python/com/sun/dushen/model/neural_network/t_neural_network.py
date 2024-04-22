import logging.config
import multiprocessing
from functools import partial

import yaml
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

from com.sun.dushen.common import utils
from com.sun.dushen.model.neural_network.neural_network import sum_red


def evaluate_model(i, j, k, X, y):
    model = MLPRegressor(hidden_layer_sizes=(i, j), random_state=k)
    scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=5)
    mean_score = -scores.mean()
    logger.debug('{}, {} {} {}'.format(mean_score, i, j, k))
    return mean_score, i, j, k


if __name__ == '__main__':
    # 加载 YAML 配置文件
    with open(utils.resources_path() + '/t_logging.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # 配置 logging 模块
    logging.config.dictConfig(config)

    # 创建日志记录器
    logger = logging.getLogger('dushen')

    df = utils.read_csv('ssq')

    # 提取特征和目标
    df['sum'] = sum_red(df)
    X = df[['sum']]
    y = df[['red1', 'red2', 'red3', 'red4', 'red5', 'red6']].values

    # 数据归一化
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    z = 10000

    num_processes = multiprocessing.cpu_count()  # 获取CPU核心数
    pool = multiprocessing.Pool(processes=num_processes)

    partial_evaluate_model = partial(evaluate_model, X=X, y=y)
    results = pool.starmap(partial_evaluate_model, [(i, j, k) for i in range(1, z) for j in range(1, z) for k in range(1, z)])

    pool.close()
    pool.join()

    # 在 results 中找到最小的 mean_score 对应的参数
    min_result = min(results)
    print("Minimum mean_score:", min_result)
