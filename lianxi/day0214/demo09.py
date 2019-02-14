# 装饰器的发展
# 1.原始
def checkuser(fun):
    username = input("请输入用户名：")
    if username == "lzj":
        print("登录成功")
        fun()
    else:
        print("登录失败")

def showlist():
    print("展示订单")
checkuser(showlist)

# 2.带有闭包
def checkuser(fun):
    def check():
        username = input("请输入用户名：")
        if username == "lzj":
            print("登录成功")
            fun()
        else:
            print("登录失败")
    return check

def showlist():
    print("展示订单")
# result = checkuser(showlist)
# result()
showlist = checkuser(showlist)
showlist()

# 3. 带有装饰器
def checkuser(fun):
    def check():
        username = input("请输入用户名：")
        if username == "lzj":
            print("登录成功")
            fun()
        else:
            print("登录失败")
    return check

@checkuser
def showlist():
    print("展示订单")
showlist()
