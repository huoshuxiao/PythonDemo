# 随机森林模型

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from com.sun.dushen.common import utils


def run_hospital():
    df = utils.read_csv('hospital')

    # 将日期列转换为 datetime 类型
    df['日期'] = pd.to_datetime(df['日期'])

    # 创建一个特征列，表示日期距离某个基准日期的天数
    base_date = pd.to_datetime('20030223')
    df['天数'] = (df['日期'] - base_date).dt.days

    # 创建特征和目标变量
    X = df[['天数']]
    y = df['就诊量']

    # 创建一个字典来存储每个科室的预测结果
    predictions = {}

    # 遍历每个科室
    for dept in df['科室'].unique():
        # 从数据中筛选出当前科室的记录
        X_dept = X[df['科室'] == dept]
        y_dept = y[df['科室'] == dept]

        # 将数据拆分为训练集和测试集
        X_train, X_test, y_train, y_test = train_test_split(X_dept, y_dept, test_size=0.001, random_state=1048)

        # 训练随机森林模型
        model = RandomForestRegressor(random_state=1048)
        model.fit(X_train, y_train)

        # 使用模型进行预测
        predicted_visits = model.predict(X_test)

        # 计算预测准确率（这里简单地用训练集上的均方根误差作为准确率指标）
        accuracy = model.score(X_test, y_test)

        # 将预测结果存储到字典中
        predictions[dept] = (predicted_visits, accuracy)

    # 打印预测结果
    for dept, (predicted_visits, accuracy) in predictions.items():
        print(f"科室: {dept}")
        print(f"预测的就诊量: {predicted_visits[0]}")
        print(f"预测准确率: {accuracy}")
        print()
