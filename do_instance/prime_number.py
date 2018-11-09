#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 判断质数（素数）
# 在大于1的自然数中，除了1和它本身以外不再有其他因数

num = int(input('输入一个整数：'))

# 质数大于1
if num > 1:
    # 查看因子
    for x in range(2, num):
        if num % x == 0:
            print(num, '不是质数')
            print(x, '*', num//x, '=', num)
            break

    else:
        print(num, '是质数')


else:
    print(num, '不是质数')

lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=',')
