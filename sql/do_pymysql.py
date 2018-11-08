#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import pymysql


# 打开数据连接
db = pymysql.connect('localhost', 'root', 'root', 'db_test')

# # 创建游标
# cursor = db.cursor()
#
# # 使用execute执行sql
# cursor.execute('SELECT VERSION()')
#
# # 使用fetchone 获取单条记录
# data = cursor.fetchone()
#
# print('Database version: %s' % data)
#
# # 关闭游标(可选)
# cursor.close()
#
# # 关闭连接
# db.close()


'''创建数据表'''
# 创建游标
cursor = db.cursor()

# 先删除表
cursor.execute("DROP TABLE IF EXISTS `employee`")

# 使用预处理语句创建表
sql = """CREATE TABLE `employee`(
    `first_name` varchar (20) NOT NULL DEFAULT '',
    `last_name` varchar (20) NOT NULL DEFAULT '',
    `age` int unsigned NOT NULL DEFAULT '0',
    `sex` char(1),
    `income` decimal(10,2) NOT NULL DEFAULT '0.00'
)ENGINE=Innodb DEFAULT CHARSET=utf8"""


# 执行sql
cursor.execute(sql)

# 关闭游标
cursor.close()

# 关闭数据库
db.close()
