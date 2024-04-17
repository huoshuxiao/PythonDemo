# 相似度

import datetime

import pandas as pd

from com.sun.dushen.common import utils
from com.sun.dushen.common.consts import FORMAT_DATE
from com.sun.dushen.model.lottery import counts


def run(random_count):
    df = utils.read_csv('ssq')
    red1 = df['red1'].to_list()
    red2 = df['red2'].to_list()
    red3 = df['red3'].to_list()
    red4 = df['red4'].to_list()
    red5 = df['red5'].to_list()
    red6 = df['red6'].to_list()

    blue1 = df['blue1'].to_list()

    date = df['date'].to_list()

    # TODO 出球号码
    bonus = counts.do_ssq_bonus(random_count)
    lastDate = datetime.date.today().strftime(FORMAT_DATE)

    redData = []
    blueData = []
    for i in range(0, len(red1)):
        row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(red6[i])]
        redData.append(','.join(row))

        row = [str(blue1[i])]
        blueData.append(','.join(row))

    result = []
    # 现有号码相似度
    i = len(redData)
    redText1Array = redData[0:i]
    blueText1Array = blueData[0:i]

    # 计算相似度
    for j in range(0, len(redText1Array)):
        text1 = redText1Array[j] + ',B' + blueText1Array[j]
        text2 = ','.join(bonus.split(',')[0:6]) + ',B' + ','.join(bonus.split(',')[6:7])
        score = similarity_score(text1, text2)

        data = {
            'date': lastDate,
            'current': text2.replace('B', ''),
            'pool': text1.replace('B', ''),
            'score': score,
            '_date': date[j],
        }
        result.append(data)

    utils.write_csv('ssq_similarity{}'.format(random_count), ['date', 'current', 'pool', 'score', '_date'], result)
    # score 分布计算
    print(pd.DataFrame.from_records(result)['score'].value_counts())


# Jaccard相似度通过计算两个集合之间的交集和并集之间的比率来衡量相似性。
def similarity_score(arr1, arr2):
    set1 = set(arr1.split(","))
    set2 = set(arr2.split(","))
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    score = len(intersection) / len(union)
    return score
