"""
类方法： 需要使用@classmethod方法声明 第一个参数为cls 可以访问类相关比如 类说明
实例方法： 方法的第一个参数为self , 用来操作实例属性
静态方法：需要使用@staticmethod声明，和类无关
"""
from day0212.utils import Utils
print(Utils.max(5,100))
class Person(object):
    """这是一个描述人的类
    这个类中有实例属性name
    """
    def __init__(self, _name):
        "声明实例属性name"
        self.name = _name

    "声明一个实例方法"
    def setname(self,  _newname):
        self.name = _newname

    "声明一个类方法"
    @classmethod
    def desc(cls):
        print(cls.__doc__)

    "声明一个静态方法"
    @staticmethod
    def log():
        print("和类无关的方法")




p1 = Person("zzy")
# p1.setname("zzy1")
# print(p1.name)

"实例可以访问类方法,类可以访问类方法"
# p1.desc()
# Person.desc()

"静态方法通过实例，类都可以访问"
# p1.log()
# Person.log()




"""
实例属性  类属性（属于类的）
1声明一个类（需要内存 存储类的信息） 此时声明类属性占一份内存1
2声明一个实例A（需要内存 存储实例A信息） 可以访问类属性可以使用内存1  需要内存2来维护实例属性
3声明一个实例B（需要内存 存储实例B的信息） 可以访问类属性可以使用内存1 需要内存3来维护实例属性
为了节省内存（多使用类属性，少使用实例属性）
"""
