# 相似度 分析
import pandas as pd

from com.sun.dushen.common import utils


def run():
    # 分析用(临时)
    # ssq()
    return ssq2()


# 全量（每期相似度）
def ssq():
    df = utils.read_csv('ssq')
    red1 = df['red1'].to_list()
    red2 = df['red2'].to_list()
    red3 = df['red3'].to_list()
    red4 = df['red4'].to_list()
    red5 = df['red5'].to_list()
    red6 = df['red6'].to_list()

    blue1 = df['blue1'].to_list()

    date = df['date'].to_list()

    redData = []
    blueData = []
    for i in range(0, len(red1)):
        row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(red6[i])]
        redData.append(','.join(row))

        row = [str(blue1[i])]
        blueData.append(','.join(row))

    result = []
    # 现有号码相似度
    for i in range(1, len(redData)):
        redText1Array = redData[0:i]
        blueText1Array = blueData[0:i]
        redText2 = redData[i]
        blueText2 = blueData[i]

        # 计算相似度
        for j in range(0, len(redText1Array)):
            text1 = redText1Array[j] + ',B' + blueText1Array[j]
            text2 = redText2 + ',B' + blueText2
            score = similarity_score(text1, text2)
            print("日期：{} 当期号码：{} 池号码：{} 相似度得分:{} ".format(date[i], text2.replace('B', ''), text1.replace('B', ''), score))

            data = {
                'date': date[i],
                'current': text2.replace('B', ''),
                'pool': text1.replace('B', ''),
                'score': score,
                '_date': date[j],
            }
            result.append(data)

    utils.write_csv('ssq_similarity', ['date', 'current', 'pool', 'score', '_date'], result)
    print(pd.DataFrame.from_records(result)['score'].value_counts())


# 最新（最新一期与之前数据的相似度）
def ssq2():
    df = utils.read_csv('ssq')
    red1 = df['red1'].to_list()
    red2 = df['red2'].to_list()
    red3 = df['red3'].to_list()
    red4 = df['red4'].to_list()
    red5 = df['red5'].to_list()
    red6 = df['red6'].to_list()

    blue1 = df['blue1'].to_list()

    date = df['date'].to_list()

    redData = []
    blueData = []
    for i in range(0, len(red1)):
        row = [str(red1[i]), str(red2[i]), str(red3[i]), str(red4[i]), str(red5[i]), str(red6[i])]
        redData.append(','.join(row))

        row = [str(blue1[i])]
        blueData.append(','.join(row))

    result = []
    i = len(redData)
    redText1Array = redData[0:i]
    blueText1Array = blueData[0:i]
    # 最后一期
    redText2 = redData[i - 1]
    blueText2 = blueData[i - 1]
    lastDate = date[i - 1]
    last_data = ''
    # 计算相似度
    for j in range(0, len(redText1Array) - 1):
        text1 = redText1Array[j] + ',B' + blueText1Array[j]
        text2 = redText2 + ',B' + blueText2
        score = similarity_score(text1, text2)
        print("日期：{} 当期号码：{} 池号码：{} 相似度得分:{} ".format(lastDate, text2.replace('B', ''), text1.replace('B', ''), score))

        data = {
            'date': lastDate,
            'current': text2.replace('B', ''),
            'pool': text1.replace('B', ''),
            'score': score,
            '_date': date[j],
        }
        result.append(data)
        last_data = data['current']

    utils.write_csv('ssq_similarity{}'.format(lastDate), ['date', 'current', 'pool', 'score', '_date'], result)
    print(pd.DataFrame.from_records(result)['score'].value_counts())
    return last_data


# Jaccard相似度通过计算两个集合之间的交集和并集之间的比率来衡量相似性。
def similarity_score(arr1, arr2):
    set1 = set(arr1.split(","))
    set2 = set(arr2.split(","))
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    score = len(intersection) / len(union)
    return score
