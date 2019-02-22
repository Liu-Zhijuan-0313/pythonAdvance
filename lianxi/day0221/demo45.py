"""
SMTP/POP3/IMAP邮件收发
2.SMTP:发邮件，属于 TCP/IP 协议簇，邮件的中转，
       它帮助每台计算机在发送或中转信件时找到下一个目的地

1.POP3:收邮件，收之后会删除邮件服务器上邮件

3.IMAP:收邮件，收之后不会删除邮件服务器上邮件
       您在电子邮件客户端收取的邮件仍然保留在服务器上，
       同时在客户端上的操作都会反馈到服务器上，
       如：删除邮件，标记已读等，
使用SMTP协议发送邮件
应为各个运营商不同需要配置不同的SMTP信息
"""

"""
1.建立连接
2，登录授权
3，实际操作
4，quit

SMTP:发邮件
POP3：收邮件，收之后会删除邮件服务器上邮件
IMAP：收邮件，不会删除邮件服务器邮件
使用SMTP协议发送邮件
应为各个运营商不同需要配置不同的SMTP信息
"""

"""
一：普通文本的邮件发送
"""
# import smtplib
# from email.mime.text import MIMEText
#
# # 1.建立连接
# smtp = smtplib.SMTP("smtp.163.com")
# # 2.登录
# smtp.login("18137128152@163.com", "qikuedu")
# # 3.发送邮件
# sender = "18137128152@163.com"
# recever = "Lzj1602176692@163.com"
# message = MIMEText("这是一封使用Python写的邮件")
# message["from"] = sender
# message["to"] = "Lzj1602176692@163.com"
# message["subject"] = "学会python发邮件"
# # 第一个参数为发件人，第二个参数为收件人，第三个参数为具体邮件内容
# smtp.sendmail(sender, recever, message.as_string())
# # 4.退出
# smtp.quit()


"""
二: 1.普通文本的邮件发送
    2.发送(带html标签的)文本邮件
    3.发送（带html标签的带图片）文本邮件
    4.发送.py文件(附件)
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
try:
    # 1.建立连接
    smtp = smtplib.SMTP("smtp.163.com")
    # 2.登录
    smtp.login("18137128152@163.com", "qikuedu")
    # 3.发送邮件
    sender = "18137128152@163.com"
    recever = "Lzj1602176692@163.com"

    # 第一种方法发送（带html标签的）文本邮件
    # message = MIMEText("<h1>这是一封使用Python写的邮件</h1>", _subtype="html")
    # 第二种方法发送（带html标签的）文本邮件
    message = MIMEMultipart()
    msghtml = MIMEText("<h1>这是一封使用Python写的邮件</h1>", _subtype="html")
    message.attach(msghtml)

    # 第三种方法发送（带html标签的带图片）文本邮件
    # message = MIMEMultipart()
    # msghtml = MIMEText("<h1>这是一封使用Python写的邮件</h1><br><img src='cid:img001'>", _subtype="html")
    # message.attach(msghtml)
    # with open("进程.png", "rb") as f:
    #     imagemsg = MIMEImage(f.read())
    #     imagemsg.add_header("Content-ID", "img001")
    #     message.attach(imagemsg)

    # 第四种方法发送.py文件(附件)
    with open("demo43.py", "rb") as f:
        pymsg = MIMEText(f.read(), "base64", "utf-8")
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        pymsg["Content-Disposition"] = 'attachment; filename = "flask.py"'
        message.attach(pymsg)


    message["from"] = sender
    message["to"] = "Lzj1602176692@163.com"
    message["subject"] = "学会python发邮件"
    # 第一个参数为发件人，第二个参数为收件人，第三个参数为具体邮件内容
    smtp.sendmail(sender, recever, message.as_string())
    # 4.退出
    smtp.quit()
except Exception as e:
    print(e)

