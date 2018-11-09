#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 判断是否为闰年
# 普通年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1999年不是闰年）；
# 世纪年:能被400整除的为世纪闰年。（如2000年是闰年，1900年不是闰年）；
# year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

import calendar

while True:
    try:
        year = int(input('请输入年份：'))
    except ValueError:
        print("输入的不是年份！")
        continue

    check_year = calendar.isleap(year)

    if check_year is True:      # 用==也可以，is和==的区别，is判断是否是同个对象，内存地址是否一样，== 判断的是内容是否相等(!=/is not)
        print('{0} 是闰年'.format(year))
    else:
        print('{0} 不是闰年'.format(year))

