"""
FTP 客户端开发
"""
from ftplib import FTP
# 1建立连接
ftp = FTP("192.168.15.33")
# 2登录
ftp.login("ftpzzy","123456")
# 3操作文件
print(ftp.getwelcome())
print(ftp.pwd())
ftp.cwd("subfolder")
print(ftp.pwd())
ftp.cwd("456")
print(ftp.pwd())
ftp.cwd("/")
print(ftp.pwd())
print(ftp.dir())
# 4退出
ftp.quit()
