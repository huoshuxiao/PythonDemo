# 次数 分析
import math
import os
from concurrent import futures

from com.sun.dushen.data.analysis import counts
from com.sun.dushen.common import utils


# 全量
def main():

    # 计算 随机数模型
    df = utils.read_csv('ssq')
    thread_count = (os.cpu_count() + 1) * 2
    data_split_size = math.ceil(len(df) / thread_count)

    body = []
    # 如果任务是CPU密集型的，即主要涉及大量计算和数据处理，应该选择进程池，以充分利用多核处理器的并行计算能力。资源占用高。
    with futures.ProcessPoolExecutor(thread_count) as executor:
        fs = []
        for i in range(0, thread_count):
            end = data_split_size * i + data_split_size
            if end > len(df):
                end = len(df)
            # 越界退出
            if end <= data_split_size * i:
                break

            f = executor.submit(counts.sub_ssq, data_split_size * i, end, df)
            fs.append(f)

        for f in futures.as_completed(fs):
            d = f.result()[0].split(',')
            row = {
                'no': d[0],
                'date': d[1],
                'red1': d[2],
                'red2': d[3],
                'red3': d[4],
                'red4': d[5],
                'red5': d[6],
                'red6': d[7],
                'blue1': d[8],
                'count': d[9],
                'count_length': len(d[9]),
            }
            body.append(row)

    utils.write_csv('ssq_count', ['no', 'date', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue1', 'count', 'count_length'], body)


if __name__ == '__main__':
    main()
