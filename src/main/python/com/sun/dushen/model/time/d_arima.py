# ARIMA模型（英语：Autoregressive Integrated Moving Average model）
# 差分整合移动平均自回归模型，又称整合移动平均自回归模型（移动也可称作滑动）
# 是时间序列预测分析方法之一

import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

from com.sun.dushen.common import utils


def run():
    df = utils.read_csv('ssq')
    # 拟合ARIMA模型并进行预测
    forecast_results = {}
    for column in df.columns:
        model = ARIMA(df[column], order=([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 4, 6))
        # model = ARIMA(df[column], order=([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], 5, [0,1]))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=1)
        forecast_results[column] = forecast[len(df)]

    # 打印预测结果
    print("预测的xx销售量为:", forecast_results['no'])
    # print("预测的苹果销售量为:", forecast_results['red1'])
    # print("预测的香蕉销售量为:", forecast_results['red2'])
    # print("预测的橘子销售量为:", forecast_results['red3'])
    # print("预测的菠萝销售量为:", forecast_results['red4'])
    # print("预测的西瓜销售量为:", forecast_results['red5'])
    # print("预测的哈密瓜销售量为:", forecast_results['red6'])
    print("预测的桃子销售量为:", forecast_results['blue1'])


# # 定义一个函数用于拟合ARIMA模型并进行预测
# def arima_forecast(data):
#     model = ARIMA(data, order=(1, 1, 0))
#     model_fit = model.fit()
#     forecast = model_fit.forecast(steps=1)[0]
#     return forecast

def chat():

    df = utils.read_csv('ssq')
    # 绘制时间序列图
    plt.figure(figsize=(10, 7))

    # plt.plot(df['date'], df['red1'], label='Apple')
    # plt.plot(df['date'], df['red2'], label='Banana')
    # plt.plot(df['date'], df['red3'], label='Orange')
    # plt.plot(df['date'], df['red4'], label='Jackfruit')
    # plt.plot(df['date'], df['red5'], label='Watermelon')
    # plt.plot(df['date'], df['red6'], label='Honeydew')
    plt.plot(df['date'], df['blue1'], label='Peach')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Fruit Sales Time Series')
    plt.legend()
    plt.show()


chat()
# run()
