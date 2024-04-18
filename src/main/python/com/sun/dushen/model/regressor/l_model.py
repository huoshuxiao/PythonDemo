# 线性/多元回归
import numpy
from sklearn import linear_model

from com.sun.dushen.common import utils


def ssq_count(no, date):
    print("双色球", no, date)

    df = utils.read_csv('count_ssq')

    X = df[['no', 'date', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue1']]
    for i in ['count']:
        y = df[i]

        ml = linear_model.LinearRegression()
        ml.fit(X, y)
        ball = ml.predict(X)

        print(i, numpy.average(ball), ml.coef_)


def ssq(no, date):
    print("双色球", no, date)#, "红球", random.sample(range(1, 34), 6), "篮球", random.sample(range(1, 17), 1))

    df = utils.read_csv('ssq')

    # r"""option 1"""
    # # X = df[['no', 'date',
    # #         'dummy_red1', 'dummy_red1', 'dummy_red3', 'dummy_red4', 'dummy_red5', 'dummy_red6', #'dummy_red7', 'dummy_red8', 'dummy_red9', 'dummy_red10',
    # #         # 'dummy_red11', 'dummy_red12', 'dummy_red13', 'dummy_red14', 'dummy_red15', 'dummy_red16', 'dummy_red17', 'dummy_red18', 'dummy_red19', 'dummy_red20',
    # #         # 'dummy_red21', 'dummy_red22', 'dummy_red23', 'dummy_red24', 'dummy_red25', 'dummy_red26', 'dummy_red27', 'dummy_red28', 'dummy_red29', 'dummy_red30',
    # #         # 'dummy_red31', 'dummy_red32', 'dummy_red33',
    # #         ]]
    # # for i in ['red1', 'red2', 'red3', 'red4', 'red5', 'red6']:
    # #     y = df[i]
    # #
    # #     ml = linear_model.LinearRegression()
    # #     ml.fit(X, y)
    # #     red = ml.predict([[no, date] + list(range(1, 34))])
    # #
    # #     print(i, red, ml.coef_)
    #
    # X = df[['no', 'date',
    #         'dummy_blue1',  # 'dummy_blue2', 'dummy_blue3', 'dummy_blue4', 'dummy_blue5', 'dummy_blue6', 'dummy_blue7', 'dummy_blue8', 'dummy_blue9', 'dummy_blue10',
    #         # 'dummy_blue11', 'dummy_blue12', 'dummy_blue13', 'dummy_blue14', 'dummy_blue15', 'dummy_blue16'
    #         ]]
    #
    # do = True
    # while do:
    #     for i in ['blue1']:
    #         y = df[i]
    #         dummy_blue = utils.randoms(16, 1)
    #
    #         ml = linear_model.LinearRegression()
    #         ml.fit(X, y)
    #         blue = ml.predict([[no, date, str(dummy_blue[0])]])
    #
    #         print(i, blue, ml.coef_, 'dummy', dummy_blue[0], 'X1', X['dummy_blue1'][1])
    #         if abs(ml.coef_[2]) >= 0.05:
    #             print(i, blue, ml.coef_, dummy_blue[0])
    #             do = False
    #         else:
    #             for k in X['dummy_blue1']:
    #                 X['dummy_blue1'][k] = utils.randoms(16, 1)[0]
    #             # print(X['dummy_blue1'])
    #             # dfd = df.copy()
    #             # for k in X['dummy_blue1']:
    #             #     dfd['dummy_blue1'][k] = utils.randoms(16, 1)[0]
    #             # df = dfd

    r"""option 2"""

    X = df[['no', 'date']]
    for i in ['red1', 'red2', 'red3', 'red4', 'red5', 'red6']:
        y = df[i]

        ml = linear_model.LinearRegression()
        ml.fit(X, y)
        red = ml.predict([[no, date]])

        print(i, red, ml.coef_)

    for i in ['blue1']:
        y = df[i]

        ml = linear_model.LinearRegression()
        ml.fit(X, y)
        blue = ml.predict([[no, date]])

        print(i, blue, ml.coef_)


def dlt(no, date):
    print("大乐透", no, date)#, "红球", random.sample(range(1, 36), 5), "篮球", random.sample(range(1, 13), 2))

    df = utils.read_csv('dlt')

    # r"""option 1"""
    # X = df[['no', 'date',
    #         'dummy_red1', 'dummy_red1', 'dummy_red3', 'dummy_red4', 'dummy_red5', #'dummy_red6', 'dummy_red7', 'dummy_red8', 'dummy_red9', 'dummy_red10',
    #         # 'dummy_red11', 'dummy_red12', 'dummy_red13', 'dummy_red14', 'dummy_red15', 'dummy_red16', 'dummy_red17', 'dummy_red18', 'dummy_red19', 'dummy_red20',
    #         # 'dummy_red21', 'dummy_red22', 'dummy_red23', 'dummy_red24', 'dummy_red25', 'dummy_red26', 'dummy_red27', 'dummy_red28', 'dummy_red29', 'dummy_red30',
    #         # 'dummy_red31', 'dummy_red32', 'dummy_red33', 'dummy_red34', 'dummy_red35',
    #         ]]
    #
    # dummy_red1 = random.sample(range(1, 36), 1)
    # dummy_red2 = random.sample(range(1, 36), 1)
    # dummy_red3 = random.sample(range(1, 36), 1)
    # dummy_red4 = random.sample(range(1, 36), 1)
    # dummy_red5 = random.sample(range(1, 36), 1)
    # for i in ['red1', 'red2', 'red3', 'red4', 'red5']:
    #     y = df[i]
    #
    #     ml = linear_model.LinearRegression()
    #     ml.fit(X, y)
    #     red = ml.predict([[no, date, dummy_red1, dummy_red2, dummy_red3, dummy_red4, dummy_red5]])
    #
    #     print(i, red, ml.coef_)

    # X = df[['no', 'date',
    #         'dummy_blue1', 'dummy_blue2', #'dummy_blue3', 'dummy_blue4', 'dummy_blue5', 'dummy_blue6', 'dummy_blue7', 'dummy_blue8', 'dummy_blue9', 'dummy_blue10',
    #         #'dummy_blue11', 'dummy_blue12'
    #         ]]
    # for i in ['blue1', 'blue2']:
    #     y = df[i]
    #
    #     ml = linear_model.LinearRegression()
    #     ml.fit(X, y)
    #     blue = ml.predict([[no, date] + list(range(1, 13))])
    #
    #     print(i, blue, ml.coef_)

    r"""option 2"""

    X = df[['no', 'date']]
    for i in ['red1', 'red2', 'red3', 'red4', 'red5']:
        y = df[i]

        ml = linear_model.LinearRegression()
        ml.fit(X, y)
        red = ml.predict([[no, date]])

        print(i, red, ml.coef_)

    for i in ['blue1', 'blue2']:
        y = df[i]

        ml = linear_model.LinearRegression()
        ml.fit(X, y)
        blue = ml.predict([[no, date]])

        print(i, blue, ml.coef_)
