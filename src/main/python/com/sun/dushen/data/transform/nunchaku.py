# 逻辑分类用数据生成
from com.sun.dushen.common import utils

data_template = {
    'no': 0, 'date': 0,
    'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0, 'R6': 0, 'R7': 0, 'R8': 0, 'R9': 0,
    'R10': 0, 'R11': 0, 'R12': 0, 'R13': 0, 'R14': 0, 'R15': 0, 'R16': 0, 'R17': 0, 'R18': 0, 'R19': 0,
    'R20': 0, 'R21': 0, 'R22': 0, 'R23': 0, 'R24': 0, 'R25': 0, 'R26': 0, 'R27': 0, 'R28': 0, 'R29': 0,
    'R30': 0, 'R31': 0, 'R32': 0, 'R33': 0,
    'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0, 'B7': 0, 'B8': 0, 'B9': 0,
    'B10': 0, 'B11': 0, 'B12': 0, 'B13': 0, 'B14': 0, 'B15': 0, 'B16': 0,
}

csv_col = ['no', 'date',
           'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9',
           'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19',
           'R20', 'R21', 'R22', 'R23', 'R24', 'R25', 'R26', 'R27', 'R28', 'R29',
           'R30', 'R31', 'R32', 'R33',
           'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
           'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16']


def run_ssq():
    """
    默认为0，中的号码为1
    
    """
    df = utils.read_csv('ssq')
    body = []
    for i in range(0, len(df)):
        row = df.iloc[i]
        no = str(row['no'])
        date = str(row['date'])
        red1 = str(row['red1'])
        red2 = str(row['red2'])
        red3 = str(row['red3'])
        red4 = str(row['red4'])
        red5 = str(row['red5'])
        red6 = str(row['red6'])
        blue1 = str(row['blue1'])

        data = dict(data_template)

        data['no'] = no
        data['date'] = date
        data['R' + red1] = 1
        data['R' + red2] = 1
        data['R' + red3] = 1
        data['R' + red4] = 1
        data['R' + red5] = 1
        data['R' + red6] = 1
        data['B' + blue1] = 1

        body.append(data)

    utils.write_csv('nunchaku', csv_col, body)


run_ssq()
