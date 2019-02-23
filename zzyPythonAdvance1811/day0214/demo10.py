"""
最终装饰是语法格式
带参数 带返回值的装饰器
"""

def checkuser(fun):
    def check(*args, **kwargs):
        username = input("请输入用户名")
        if username == "wzk":
            return fun(*args, **kwargs)
        else:
            print("未授权")
    return check
@checkuser
def showlist(n, all):
    print("展示订单列表第"+str(n)+"页,共有"+str(all)+"页")
@checkuser
def showmoney():
    print("显示余额")
@checkuser
def showinfo():
    return "hello"

showlist(10,100)
showmoney()
print(showinfo())
