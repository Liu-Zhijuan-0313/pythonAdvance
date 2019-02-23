import smtplib
from email.mime.text import MIMEText
# 1建立连接
smtp = smtplib.SMTP("smtp.163.com")
# 2 登录
smtp.login("18137128152@163.com", "******")
# 3 发送邮件
sender = "18137128152@163.com"
recever = "zhangzhaoyu@qikux.com"
message = MIMEText("这是一封使用<h1>Python</h1>写的邮件",_subtype="html")
message["from"] = sender
message["to"] = "aaaaa@qqq.com"+","+"496575233@qq.com"
message["subject"] = "学会发邮件"
smtp.sendmail(sender,[recever, "496575233@qq.com"],message.as_string())
# 4 退出
smtp.quit()