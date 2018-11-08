#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import cmath  # 复数数学模块


# 求平方根, 可以使用math模块, 负数和复数只能使用cmath
num = input('请输入一个数字：')

num_sqrt = abs(float(num)) ** 0.5
num_math_sqrt = math.sqrt(abs(float(num)))
print('{0} 绝对值的平方根为 {1} math模块的结果为 {2}'.format(num, num_sqrt, num_math_sqrt))


# 计算实数和复数平方根
complex_sqrt = cmath.sqrt(int(num))
print('{0} 的平方根为 {1:0.3f} + {2:0.3f}j'.format(num, complex_sqrt.real, complex_sqrt.imag))


# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b ** 2) - (4 * a * c)

# 两个解
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))
