# 神经网络
import logging.config

import numpy
import yaml
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

from com.sun.dushen.common import utils


def sum_red(df):
    result = []
    for i in range(0, len(df)):
        red1 = df.iloc[i]['red1']
        red2 = df.iloc[i]['red2']
        red3 = df.iloc[i]['red3']
        red4 = df.iloc[i]['red4']
        red5 = df.iloc[i]['red5']
        red6 = df.iloc[i]['red6']

        result.append(red1 + red2 + red3 + red4 + red5 + red6)

    return result


def run():
    df = utils.read_csv('ssq')

    # 提取特征和目标
    df['sum'] = sum_red(df)
    X = df[['sum']]
    y = df[['red1', 'red2', 'red3', 'red4', 'red5', 'red6']].values

    # 数据归一化
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # 创建神经网络模型
    # model = MLPRegressor(hidden_layer_sizes=(100, 100), random_state=100)

    # TODO 验证模型参数
    z = 70
    t = 60
    for i in range(z, 0, -1):
        for j in range(z, 0, -1):
            for k in range(z, 0, -1):

                if i <= t and j <= t and k <= t:
                    continue

                # 创建神经网络模型
                model = MLPRegressor(hidden_layer_sizes=(i, j), random_state=k)

                # 使用交叉验证评估模型性能
                # 以MSE为例，scoring可以根据需要改成'neg_mean_squared_error'来计算RMSE
                scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=5)

                # 取平均得分（注意取了负值，因为cross_val_score默认返回负值）
                mean_score = -scores.mean()

                # 打印均方误差（MSE）或均方根误差（RMSE）
                logger.debug('mean_score :: {}, {} {} {}'.format(mean_score, i, j, k))

    # # 训练模型
    # model.fit(X_train, y_train)
    #
    # # 使用模型生成号码
    # recommended_numbers = model.predict(X_test)[:5]
    # print("推荐号码:", recommended_numbers)


# 加载 YAML 配置文件
with open(utils.resources_path() + '/logging.yaml', 'r') as file:
    config = yaml.safe_load(file)

# 配置 logging 模块
logging.config.dictConfig(config)

# 创建日志记录器
logger = logging.getLogger('dushen')
run()
