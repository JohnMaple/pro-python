#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Filename : fibonacci.py
# Author by : Alex

nterms = int(input('你需要几项？'))


def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield a
        a, b = b, a + b
        n = n + 1
    return 'done'


def recur_fibo(n):
    """
    递归函数 输出斐波那契数列
    :param n:
    :return:
    """
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)


print("斐波那契数列：")
for x in fib(nterms):
    print(x, end=',')
print()
print('-----------------------------')
for i in range(nterms):
    print(recur_fibo(i), end=',')


