# 4.装饰器有参数
def checkuser(fun):
    def check(n):
        username = input("请输入用户名：")
        if username == "lzj":
            print("登录成功")
            fun(n)
        else:
            print("登录失败")
    return check

@checkuser
def showlist(n):
    print("展示订单"+str(n)+"页")
showlist(2)

# 5.装饰器有多个参数
def checkuser(fun):
    def check(m, all):
        username = input("请输入用户名：")
        if username == "lzj":
            print("登录成功")
            fun(m, all)
        else:
            print("登录失败")
    return check

@checkuser
def showlist(n, all):
    print("展示订单"+str(n)+"页", "总页数"+str(all))
showlist(2, 10)


# 6.装饰器有多个参数，注意return fun(*args)
def checkuser(fun):
    def check(*args):
        username = input("请输入用户名：")
        if username == "lzj":
            print("登录成功")
            return fun(*args)
        else:
            print("登录失败")
    return check

@checkuser
def showlist(n, all):
    print("展示订单"+str(n)+"页", "总页数"+str(all))
showlist(2, 10)

@checkuser
def showmoney():
    print("显示金额")
showmoney()

@checkuser
def showinfo():
    return "hello"
print(showinfo())
