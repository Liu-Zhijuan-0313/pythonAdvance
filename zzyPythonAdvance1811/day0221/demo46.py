"""
1.建立连接
2，登录授权
3，实际操作
4，quit
"""
# import ftplib
# ftp = ftplib.FTP("192.168.15.33")
# ftp.login("ftpzzy","123456")
# # ftp.mkd()
# ftp.quit()
# 邮件相关协议
"""
SMTP:发邮件
POP3：收邮件，收之后会删除邮件服务器上邮件
IMAP：收邮件，不会删除邮件服务器邮件
使用SMTP协议发送邮件
应为各个运营商不同需要配置不同的SMTP信息
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart

try:
    smtp = smtplib.SMTP("smtp.163.com")
    useremail = "18137128152@163.com"
    smtp.login(useremail, "qikuedu")

    # 第一个参数为发件人，第二个参数为收件人列表，第三个参数为具有邮件内容
    # msginfo = MIMEText("这是一封测试<h1>邮件</h1>","html")
    msginfo = MIMEMultipart()

    htmlmsg = MIMEText("这是文本<h1>部分</h1> <br> <img src='cid:img001'>","html")
    msginfo.attach(htmlmsg)

    with open("message.png", "rb") as f:
        imgmsg = MIMEImage(f.read())
        imgmsg.add_header("Content-ID","img001")
        msginfo.attach(imgmsg)

    with open("demo42.py","rb") as f:
        pymsg = MIMEText(f.read(),"base64","utf-8")
        pymsg["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        pymsg["Content-Disposition"] = 'attachment; filename="fujian.py"'
        msginfo.attach(pymsg)



    msginfo["from"] = useremail
    msginfo["to"] = useremail+","+"zhangzhaoyu@qikux.com,496575233@qq.com"
    msginfo["subject"] = "测试图片"
    smtp.sendmail(useremail, [useremail, "zhangzhaoyu@qikux.com", "496575233@qq.com"], msginfo.as_string())
    smtp.quit()
except Exception as e:
    print(e)