"""
类装饰器:
类装饰器通过构造方法以及call方法来实现
当程序检测到函数有类装饰器时没有直接执行函数，将函数作为参数传递个类的构造函数
当该函数调用时会执行类的call函数
"""


class CheckUser:
    def __init__(self, fun):
        print("构造方法")
        self.f = fun

    def __call__(self, *args, **kwargs):
        print("call方法")
        self.f()

"使用实例名（）会执行类内部call方法"
# cu = CheckUser()
# cu()

@CheckUser
def login():
    print("登陆了")
login()
