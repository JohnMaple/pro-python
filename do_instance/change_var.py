#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 变量交换
x = 1
y = 9

print(x)
print(y)
print('------------------')

tmp = x
x = y
y = tmp

print(x)
print(y)
print('------------------')

x, y = y, x

print(x)
print(y)
print('------------------')

x = x + y
y = x - y
x = x - y

print(x)
print(y)
print('------------------')

x = x ^ y
y = x ^ y
x = x ^ y

print(x)
print(y)
print('------------------')
