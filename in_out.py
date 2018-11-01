#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle


f = open('./files/test.txt', 'wb')
d = dict(name='bob', age=20, score=88)
pickle.dump(d, f)
f.close()

f = open('./files/test.txt', 'rb')
arr = pickle.load(f)
f.close()
print(arr)
