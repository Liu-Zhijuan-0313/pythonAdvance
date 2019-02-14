# 2.实现需求：给订单列表，用户余额两个函数添加装饰函数，能够完成权限验证功能

# 1.原始
# def checkuser():
#     username = input("请输入用户名：")
#     if username == "lzj":
#         print("登录成功")
#         showlist()
#         showmoney()
#     else:
#         print("未授权，登录失败")
#
#
# def showlist():
#     print("订单列表")
# def showmoney():
#     print("用户余额")
# checkuser()

# 2.带闭包
# def checkuser(fun):
#     def check():
#         username = input("请输入用户名：")
#         if username == "lzj":
#             print("登录成功")
#             fun()
#         else:
#             print("未授权，登录失败")
#     return check
#
# def showlist():
#     print("订单列表")
# showlist = checkuser(showlist)
# showlist()
# def showmoney():
#     print("用户余额")
# showmoney = checkuser(showmoney)
# showmoney()

# 3.带装饰器
def checkuser(fun):
    def check():
        username = input("请输入用户名：")
        if username == "lzj":
            print("登录成功")
            fun()
        else:
            print("未授权，登录失败")
    return check

@checkuser
def showlist():
    print("订单列表")
showlist()

@checkuser
def showmoney():
    print("用户余额")
showmoney()