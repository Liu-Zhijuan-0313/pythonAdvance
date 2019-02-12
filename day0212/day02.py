"""
类方法： 需要使用@classmethod方法声明 第一个参数为cls 可以访问类相关比如 类说明
实例方法： 方法的第一个参数为self , 用来操作实例属性
静态方法：需要使用@staticmethod声明，和类无关
"""
from day0212.utils import Utils
print(Utils.max(10, 20))


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


a1 = Person("lzj")
print(a1.name)
# 实例可以访问实例方法,类不可以访问实例方法
a1.eat()
# 实例可以访问类方法,类也可以访问类方法
a1.desc()
Person.desc()
