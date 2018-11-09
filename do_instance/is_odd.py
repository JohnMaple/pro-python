#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数


while True:
    try:
        num = int(input('输入一个整数：'))     # 判断输入是否为整数

    except ValueError:  # 不是纯数字需要重新输入
            print("输入的不是整数！")
            continue

    if num % 2 == 0:
        print("{0} 是偶数".format(num))
    else:
        print("{} 是奇数".format(num))     # 如果只有一个数，可以不用下标

