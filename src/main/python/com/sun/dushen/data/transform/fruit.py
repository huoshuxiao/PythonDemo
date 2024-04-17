# 生成式数据

from com.sun.dushen.common import utils

row_template = '水果店{}销售额为{}元，其中苹果{}份，香蕉{}份，橘子{}份，橙子{}份，西瓜{}份，哈密瓜{}份，桃子{}份。\n\n###\n\n'


def run_ssq():
    df = utils.read_csv('count_ssq')
    body = []
    for i in range(0, len(df)):
        row = df.iloc[i]
        date = str(row['date'])
        count = str(row['count'])
        red1 = str(row['red1'])
        red2 = str(row['red2'])
        red3 = str(row['red3'])
        red4 = str(row['red4'])
        red5 = str(row['red5'])
        red6 = str(row['red6'])
        blue1 = str(row['blue1'])

        data = {
            'fruit': row_template.format(date, count, red1, red2, red3, red4, red5, red6, blue1)
        }
        body.append(data)

    utils.write_csv('fruit', ['fruit'], body)
