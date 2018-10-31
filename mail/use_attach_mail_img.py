#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr, formataddr


# 先定义署名格式化函数
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 发送人，接收人
sender = '840240xxx@qq.com'
pwd = 'xxxxxxxxxxxxx'         # 请自行登陆邮箱打开SMTP服务，会自动生成第三方授权码，不是登陆密码！
receiver = '924348xxx@qq.com'

# 格式化的署名和接收人信息
message=MIMEMultipart()
message['From'] = _format_addr('这是xx<%s>'%sender)
message['To'] = _format_addr(receiver)
message['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
message.attach(MIMEText('<html><body>'+'<h1>Hello</h1>'+'<p>礼物<img src="cid:Imgid">'+'</body></html>', 'html', 'utf-8'))

# MIMEImage，只要打开相应图片，再用read()方法读入数据，指明src中的代号是多少，如这里是'Imgid’，在HTML格式里就对应输入。
with open('d:/documents/pictures/V_mode.jpg', 'rb') as f:
    mime = MIMEImage(f.read())
    mime.add_header('Content-ID','Imgid')
    message.attach(mime)

# 发送邮件！
try:
    smtpobj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtpobj.login(sender, pwd)
    smtpobj.sendmail(sender, [receiver], message.as_string())
    print('邮件发送成功')
    smtpobj.quit()
except smtplib.SMTPException as e:
    print('邮件发送失败，Case:%s' % e)
