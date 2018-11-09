#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 阶乘：n! = 1*2*3*...*n,(n>=0),0!=1

num = int(input('输入一个数字：'))
factorial = 1

# 是否为负数，负数没有阶乘
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print('0的阶乘为1')
else:
    for i in range(1, num+1):
        factorial *= i
    print("%d！= %d" % (num, factorial))


# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{} x {} = {}\t'.format(j, i, i*j), end='')   # 可以不用下标
    print()
