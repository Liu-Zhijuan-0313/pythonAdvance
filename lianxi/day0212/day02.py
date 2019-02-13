"""
类方法： 需要使用@classmethod方法声明 第一个参数为cls 可以访问类相关比如 类说明
实例方法： 方法的第一个参数为self , 用来操作实例属性
静态方法：需要使用@staticmethod声明，和类无关
"""
from lianxi.day0212.utils import Utils
print(Utils.max(10, 20))
print(Utils.pow(2, 3))

class Person:

    """
    这是一个类!!!!
    """
    def __init__(self, _name):
        self.name = _name

    # 实例方法
    def eat(self):
        print("吃饭")

    # 类方法
    @classmethod
    def desc(cls):
        print(cls.__doc__)
        print(cls.__dict__)

    # 静态方法
    @staticmethod
    def min(a, b):
        if a > b:
            print(b)
        else:
            print(a)


a1 = Person("lzj")
print(a1.name)
# 1.实例可以访问实例方法,类不可以访问实例方法
a1.eat()
# 2.实例和类都可以访问类方法
a1.desc()
Person.desc()
# 3.实例和类都可以访问静态方法
a1.min(1, 2)
Person.min(1, 2)

"""
实例属性  类属性（属于类的）
1声明一个类（需要内存 存储类的信息） 此时声明类属性占一份内存1
2声明一个实例A（需要内存 存储实例A信息） 可以访问类属性可以使用内存1  需要内存2来维护实例属性
3声明一个实例B（需要内存 存储实例B的信息） 可以访问类属性可以使用内存1 需要内存3来维护实例属性
为了节省内存（多使用类属性，少使用实例属性）
"""
