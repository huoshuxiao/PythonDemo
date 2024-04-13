from com.sun.dushen.common import utils

ssq_row_template = '''
{},内科,{}
{},外科,{}
{},儿科,{}
{},妇产科,{}
{},骨科,{}
{},口腔科,{}
{},皮肤科,{}
'''


def run_ssq():
    df = utils.read_csv('ssq')
    body = []
    for i in range(0, len(df)):
        row = df.iloc[i]
        date = str(row['date'])
        red1 = str(row['red1'])
        red2 = str(row['red2'])
        red3 = str(row['red3'])
        red4 = str(row['red4'])
        red5 = str(row['red5'])
        red6 = str(row['red6'])
        blue1 = str(row['blue1'])

        data = {
            '日期': date,
            '科室': '内科',
            '就诊量': red1,
        }
        body.append(data)

        data = {
            '日期': date,
            '科室': '外科',
            '就诊量': red2,
        }
        body.append(data)

        data = {
            '日期': date,
            '科室': '儿科',
            '就诊量': red3,
        }
        body.append(data)

        data = {
            '日期': date,
            '科室': '妇产科',
            '就诊量': red4,
        }
        body.append(data)

        data = {
            '日期': date,
            '科室': '骨科',
            '就诊量': red5,
        }
        body.append(data)

        data = {
            '日期': date,
            '科室': '口腔科',
            '就诊量': red6,
        }
        body.append(data)

        data = {
            '日期': date,
            '科室': '皮肤科',
            '就诊量': blue1,
        }
        body.append(data)

    utils.write_csv('hospital', ['日期', '科室', '就诊量'], body)


run_ssq()
