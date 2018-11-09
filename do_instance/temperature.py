#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def format_temperature(tem, u='F'):
    """温度转换"""
    tem = float(tem)
    if u in ['F', 'f']:
        res = (tem * 1.8) + 32
    else:
        res = (tem - 32) / 1.8

    return res, u.upper()


temperature = float(input('请输入温度：'))
unit = input('需要转换成的温度(f:华氏,c:摄氏度)')

result, un = format_temperature(temperature, unit)

print('转换结果：%.1f %s' % (result, un))
