#!/usr/bin/python3
# -*- coding: utf-8 -*-


def is_numberic(s):
    """判断字符串是否为数字，Unicode编码等"""
    try:
        float(s)    # 对字符串出现值错误
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试字符串
print(is_numberic('foo'))
print(is_numberic('1'))
print(is_numberic(1))
print(is_numberic('1.3'))
print(is_numberic('-1.3'))
print(is_numberic('1e3'))   # 1000.0
# print(is_numberic(None))
print(is_numberic(True))    # True
print(is_numberic(False))   # True
print(is_numberic('True'))

print('--------------------------')
# 测试 Unicode
print(is_numberic('٥'))     # True
# 泰语 2
print(is_numberic('๒'))     # True
# 中文数字
print(is_numberic('四'))     # True
# 版权号
print(is_numberic('©'))     # False

