# - *- coding: utf- 8 - *-
import sys

from com.sun.dushen.model import model

args = sys.argv[1:]
# 随机数模型
if len(args) == 2 and int(args[1]) > 0:
    if int(args[1]) <= 5:
        # 默认模型
        model.run()
    else:
        # 指定随机数模型
        model.run(int(args[1]))

# TODO
# model.run_analysis()
model.price()

