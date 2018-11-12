#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 最大公约数和最小公倍数
import math


def hcf(x, y):
    """
    最大公约数（穷举法）
    :param x:
    :param y:
    :return:
    """
    smaller = x if x < y else y     # 三目运算，和其他语言不同

    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            hc = i

    return hc


def hcf2(x, y):
    """
    最大公约数（辗转相除法）
    :param x:
    :param y:
    :return:
    """
    # 如果最终余数为0 公约数就计算出来了
    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x


def lcm(x, y):
    """
    最小公倍数
    :param x:
    :param y:
    :return:
    """
    greater = x if x > y else y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lc = greater
            break
        greater += 1

    return lc


num1 = int(input('输入第一个数字：'))
num2 = int(input('输入第二个数字：'))

print(num1, '和', num2, '的最大公约数为 ', hcf(num1, num2))
print(num1, '和', num2, '的最小公倍数为 ', lcm(num1, num2))
print('-------------math--------------')
print(num1, '和', num2, '的最大公约数为 ', math.gcd(num1, num2))
print(num1, '和', num2, '的最小公倍数为 ', num1 * num2 / math.gcd(num1, num2))
