#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json


d = dict(name='john', age=20, score=99)
json_str = json.dumps(d)
print(json_str)
