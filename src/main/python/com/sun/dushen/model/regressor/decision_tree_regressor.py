# 决策树模型

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

from com.sun.dushen.common import utils


def test_nunchaku():
    # 读取数据
    df = utils.read_csv('nunchaku')

    # TODO 变量分类错误

    # 提取特征(自变量)
    x = df[['no', 'date',
            'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9',
            'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19',
            'R20', 'R21', 'R22', 'R23', 'R24', 'R25', 'R26', 'R27', 'R28', 'R29',
            'R30', 'R31', 'R32', 'R33']]
    # 目标变量(因变量)
    y = df['B16']

    # 将日期转换为数值类型（如果日期是字符串类型的话）
    # X['date'] = pd.to_datetime(X['date']).astype(int)

    # 对分类特征进行独热编码
    x = pd.get_dummies(x)

    # i = 100
    for i in range(0, 5000):
        # 划分训练集和测试集
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=30, random_state=i)

        # 创建决策树模型
        model = DecisionTreeRegressor()

        # 训练模型
        model.fit(x_train, y_train)

        # 在测试集上进行预测
        y_pred = model.predict(x_test)

        # 计算均方误差（MSE）
        mse = mean_squared_error(y_test, y_pred)
        print('{} >>, nunchaku Mean Squared {}'.format(i, mse))


def test_hospital():
    # 读取数据
    df = utils.read_csv('hospital')

    # 提取特征和目标变量
    x = df[['日期', '科室']]
    y = df['就诊量']

    # 将日期转换为数值类型（如果日期是字符串类型的话）
    # x['日期'] = pd.to_datetime(X['日期']).astype(int)

    # 对分类特征进行独热编码
    x = pd.get_dummies(x)

    for i in range(15000, 20000):
        # for i in range(7000, 8000):
        # i = 4043
        # 划分训练集和测试集
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=30, random_state=i)

        # 创建决策树模型
        model = DecisionTreeRegressor()

        # 训练模型
        model.fit(x_train, y_train)

        # 在测试集上进行预测
        y_pred = model.predict(x_test)

        # 计算均方误差（MSE）
        mse = mean_squared_error(y_test, y_pred)
        print('{} >>, hospital Mean Squared {}'.format(i, mse))


def run_hospital():
    # 读取数据
    df = utils.read_csv('hospital')

    # 将日期列转换为 datetime 类型
    df['日期'] = pd.to_datetime(df['日期'])

    # 创建一个特征列，表示日期距离某个基准日期的天数
    base_date = pd.to_datetime('20030223')
    df['天数'] = (df['日期'] - base_date).dt.days

    # 创建特征和目标变量
    x = df[['天数']]
    y = df['就诊量']

    # i = 4043
    i = 17712
    # for i in range(1, 100):
    #     print(f"index: {i}")
    # 创建一个字典来存储每个科室的预测结果
    predictions = {}

    # 遍历每个科室
    for dept in df['科室'].unique():
        # 从数据中筛选出当前科室的记录
        x_dept = x[df['科室'] == dept]
        y_dept = y[df['科室'] == dept]

        # 将数据拆分为训练集和测试集
        x_train, x_test, y_train, y_test = train_test_split(x_dept, y_dept, test_size=30, random_state=i)

        # 训练决策树模型
        model = DecisionTreeRegressor(random_state=i)
        model.fit(x_train, y_train)

        # 使用模型进行预测
        predicted_visits = model.predict(x_test)

        # 计算预测准确率（这里简单地用训练集上的均方根误差作为准确率指标）
        accuracy = model.score(x_test, y_test)

        # 将预测结果存储到字典中
        predictions[dept] = (predicted_visits, accuracy)

    """
    生成的数据和线性回归类似。
    """
    # 打印预测结果
    for dept, (predicted_visits, accuracy) in predictions.items():
        print(f"科室: {dept}")
        print(f"预测的就诊量: {predicted_visits[0]}")
        print(f"预测准确率: {accuracy}")
        print()
