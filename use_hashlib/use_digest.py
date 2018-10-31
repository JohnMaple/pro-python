#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import hashlib
import hmac


md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

message = 'Hello, world!'
key = 'salt'
h = hmac.new(key.encode('utf-8'), message.encode('utf-8'), digestmod='MD5')
print(h.hexdigest())
