#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Filename : armstrong.py
# Author by : Alex

# 检测用户输入的数字是否为阿姆斯特朗数
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数， 例如1^3 + 5^3 + 3^3 = 153

# 获取用户输入
lower = int(input("最小值: "))
upper = int(input("最大值: "))


for num in range(lower, upper+1):
    # 初始化变量
    total = 0

    # 幂
    n = len(str(num))   # 数字不可迭代，字符串可以，len(iter)

    temp = num
    while temp > 0:
        digit = temp % 10   # 获取个位
        total += digit ** n
        temp //= 10     # 向下取整获取剩余的

    if num == total:
        print(num, end=' ')

