#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


def scanDir(path=os.curdir):
    path = os.path.realpath(path)
    __list = []
    for item in os.listdir(path):
        item = os.path.join(path, item)
        # @todo 查找、过滤等
        if os.path.isdir(item):
            __list += scanDir(item)
        else:
            __list.append(item)
    return __list


if __name__ == '__main__':
    list_dir = scanDir('.')
    print(list_dir)
