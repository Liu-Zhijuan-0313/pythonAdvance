""""
hashlib加密模块
"""
import hashlib
password = input("请输入密码：")
# 获取md5对象 ()
md5 = hashlib.md5()
# # 加密 切记要指定编码 encode('utf-8')
md5.update(password.encode("utf-8"))
# # 用hexdigest()获取计算的md5值
print("密码加密：", md5.hexdigest())


# import time
# import hashlib
# m = hashlib.md5(str(time.time()).encode("utf-8"))
# print("当前时间加密：", m.hexdigest())