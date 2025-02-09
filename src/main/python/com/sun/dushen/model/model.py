import datetime

from com.sun.dushen.data.analysis import t_counts as a_counts
from com.sun.dushen.common import utils
from com.sun.dushen.common.consts import FORMAT_DATE
from com.sun.dushen.data.transform import fruit
from com.sun.dushen.model.lottery import probability, counts
from com.sun.dushen.model.regressor import l_model, decision_tree_regressor


def test():
    fruit.run_ssq()


def run_analysis():
    # # step 1
    # """ 最新一期相似度 """
    # last_data = similarity.run()
    # """ 最新一期 随机次数 """
    # a_counts.ssq_count([last_data])

    # step 2
    """ 多元回归 随机次数 """
    a_counts.run_ssq_count()
    # run_ssq_count()


def run(count=5):
    """ count : default foreach 5 counts """
    run_dlt(count)
    run_ssq(count)


def run_dlt(count):
    bonus_weekday = [1, 3, 6, 5]
    today = datetime.date.today()
    weekday = today.isoweekday()
    if weekday in bonus_weekday:
        df = utils.read_csv('dlt')
        no = max(df['no'].to_list()) + 1
        if weekday == 5:
            today = today + datetime.timedelta(days=1)

        # 多元回归
        l_model.dlt(no, int(today.strftime(FORMAT_DATE)))

        # 概率
        probability.dlt()

        red1 = df['red1'].to_list()
        red1.reverse()
        red2 = df['red2'].to_list()
        red2.reverse()
        red3 = df['red3'].to_list()
        red3.reverse()
        red4 = df['red4'].to_list()
        red4.reverse()
        red5 = df['red5'].to_list()
        red5.reverse()
        blue1 = df['blue1'].to_list()
        blue1.reverse()
        blue2 = df['blue2'].to_list()
        blue2.reverse()

        data = []
        for i in range(0, count):
            row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(blue1[i]), str(blue2[i])]
            data.append(','.join(row))
        data.reverse()

        # 随机次数
        counts.dlt2One(data)


def run_ssq(count):
    bonus_weekday = [2, 4, 7, 5]
    today = datetime.date.today()
    weekday = today.isoweekday()
    if weekday in bonus_weekday:
        df = utils.read_csv('ssq')
        no = max(df['no'].to_list()) + 1
        if weekday == 5:
            today = today + datetime.timedelta(days=2)

        # 多元回归
        l_model.ssq_count(no, int(today.strftime(FORMAT_DATE)))

        # 概率
        probability.ssq()

        red1 = df['red1'].to_list()
        red1.reverse()
        red2 = df['red2'].to_list()
        red2.reverse()
        red3 = df['red3'].to_list()
        red3.reverse()
        red4 = df['red4'].to_list()
        red4.reverse()
        red5 = df['red5'].to_list()
        red5.reverse()
        red6 = df['red6'].to_list()
        red6.reverse()
        blue1 = df['blue1'].to_list()
        blue1.reverse()

        data = []
        for i in range(0, count):
            row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(red6[i]), str(blue1[i])]
            data.append(','.join(row))
        data.reverse()

        # 随机次数
        counts.ssq2One(data)


def run_ssq2(count):
    df = utils.read_csv('ssq')

    no = max(df['no'].to_list()) + 1
    print("双色球", no, datetime.date.today().strftime(FORMAT_DATE))

    red1 = df['red1'].to_list()
    red1.reverse()
    red2 = df['red2'].to_list()
    red2.reverse()
    red3 = df['red3'].to_list()
    red3.reverse()
    red4 = df['red4'].to_list()
    red4.reverse()
    red5 = df['red5'].to_list()
    red5.reverse()
    red6 = df['red6'].to_list()
    red6.reverse()
    blue1 = df['blue1'].to_list()
    blue1.reverse()

    data = []
    for i in range(0, count):
        row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(red6[i]), str(blue1[i])]
        data.append(','.join(row))
    data.reverse()

    # 随机次数
    return do_ssq_bonus(data)


def do_ssq_bonus(data):
    bonus = counts.ssq2One(data)
    print('run counts', datetime.datetime.now().isoformat(timespec='seconds'), globals()['bonus_count'])

    # TODO
    # if '5,8,16,17,21,25,12' == bonus:
    print('Winning', globals()['bonus_count'], '::', bonus)
    # else:
    #     globals()['bonus_count'] = globals()['bonus_count'] + 1
    #     do_ssq_bonus(data)
    return bonus


def run_ssq_count():
    df = utils.read_csv('ssq')
    no = max(df['no'].to_list()) + 1
    # 多元回归
    l_model.ssq_count(no, int(datetime.date.today().strftime(FORMAT_DATE)))


def regressor():
    # decision_tree_regressor.test_hospital()
    # decision_tree_regressor.run_hospital()

    decision_tree_regressor.test_nunchaku()
