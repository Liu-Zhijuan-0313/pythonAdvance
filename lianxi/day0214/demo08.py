"""
装饰器的作用：在不改变原函数的情况下给函数增加功能
装饰器由闭包和语法糖组成
@函数名 是python的一种语法糖。
开闭原则：面向扩展开放，面向编程关闭
"""


def checkuser(fun):
    def login():
        name = input("请输入你的用户名：")
        if name == "lzj":
            fun()
        else:
            print("登录失败")
    return login

@checkuser
def showlist():
    for i in range(10):
        print("订单", str(i))
@checkuser
def showmoney():
    print("你当前有余额10000￥")

@checkuser
def showdiacount():
    print("你有优惠券100 200 300 500")
showlist()
showmoney()
showdiacount()

"""
@函数名执行逻辑
检测到需要执行的函数showlist 拥有装饰器@checkuser
不执行showlist 而是将showlist 作为参数传入checkuser方法，
并且执行checkuser 方法 此时fun=showlist
将checkuser的执行结果返回，即将login方法的引用返回，即实际执行的是login方法
"""