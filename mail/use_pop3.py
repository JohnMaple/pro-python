#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib

# 输入邮件地址、口令和pop3服务器地址
email = input('Email:')
password = input('Password:')
pop3_server = input('Pop3 server:')

# 连接到POP3服务器
server = poplib.POP3(pop3_server)
# 打开或关闭调试信息
server.set_debuglevel(1)

# 打印欢迎