class Dog:
    def __del__(self):
        print("-----英雄over------")


dog1 = Dog()
dog2 = dog1

del dog1  # 不会调用 __del__方法,因为这个对象 还有其他的变量指向它,即 引用计算不是0
del dog2  # 此时会调用__del__方法,因为没有变量指向它了
print("====================")
# 如果在程序结束时,有些对象还存在,
# 那么python解释器会自动调用它们的__del__方法来完成清理工作

"""
当使用print输出对象的时候，只要自己定义了__str__(self)方法，
那么就会打印从在这个方法中return的数据
__str__方法需要返回一个字符串，当做这个对象的描写
"""

"""
1.__init__构造方法
2.__del__析构：回收时调用
"""
import time
class A():
    name = "lzj"

    def __init__(self):
        print("构造方法")

    def __del__(self):
        print("析构：回收时调用")
        print(self.name)


a = A()  # 引用计数为1
b = a   # 引用计数为2

"不会调用 __del__方法,因为这个对象 还有其他的变量指向它,即A()引用计算不是0"
del a   # 引用计数为1
time.sleep(2)

"此时会调用__del__方法,因为没有变量指向它了"
del b   # 引用计数为0
time.sleep(2)
"""
如果在程序结束时,有些对象还存在,
那么python解释器会(自动调用)它们的__del__方法来完成清理工作
"""

"""
第一个案例：
    3.__repr__返回一个对象的描述信息
    4.__str__返回一个对象的描述信息
"""
"""
当使用print输出对象的时候，只要自己定义了__str__(self)方法，
那么就会打印从在这个方法中return的数据
__str__方法需要返回一个字符串，当做这个对象的描写
"""

"""
当我们想所有环境下都统一显示的话，可以重构__repr__方法；
当我们想在不同环境下支持不同的显示，例如终端用户显示使用__str__，
而程序员在开发期间则使用底层的__repr__来显示，
实际上__str__只是覆盖了__repr__以得到更友好的用户显示
"""
from datetime import datetime as dt

print(dt.today().__repr__())


class B():

    def __init__(self, _name):
        self.name = _name

    def __str__(self):
        "返回一个对象的描述信息"
        return self.name

    def __repr__(self):
        # return "这是类A的另一种描述"
        return self.name


b = B("lzj")
print(b.__repr__())
print(b)

"""
第二个案例：
    3.str是显示给用户用的
    4.repr是给机器用的。
"""


class A(object):
    def __str__(self):
        return "this is A class"

    def __repr__(self):
        return "this is repr func"


a = A()
print(a)
print(a.__repr__())
"""
比如print(a)
调用的是a的__str__方法
而如果你在python解释器里直接敲a后回车，
调用的是a.__repr__()方法 
"""

