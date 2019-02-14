def checkuser(fun):
    def check(*args, **kwargs):
        username = input("请输入用户名：")
        if username == "lzj":
            print("登录成功")
            fun(*args, **kwargs)
        else:
            print()
    return check


@checkuser
def showlist(n, all, age=20, gender=""):
    print("订单列表"+str(n), "总订单" + str(all), "年龄是：", age, "性别：", gender)
showlist(2, 10, age=22, gender="nv")
