# 元类就是用来创建类的“东西”。
# Python中类也是一种对象。
# 使用type方法查看类类型<class 'type'>
# type拥有创建类的功能

"""
Python一切皆对象
类Stu：创建对象s1
类Stu也是一个对象
元类：创建类Person
元类：创建元类
type 创建了type
type 创建了 Person类（对象）
Person类创建了per对象
"""
import types
class Stu:
    def __init__(self):
        print("元类")


s1 = Stu()
print(type(s1), s1.__class__, Stu.__class__, type.__class__)

# 第一个参数为类名字符串 第二个参数为 父类元组,
# 第三个参数为该类的属性字典格式
P = type("Person", (), {"name": "lzj"})
print(P, type(P), P.__class__, P.__name__)

# 添加类属性
P.age = 20
per = P()
print(P, type(P), P.__class__, P.__name__)
print(P.age, per.age)

# 添加实例属性
per.gender = "nv"
print(per.gender)

# 添加类方法
@classmethod
def tea(cls):
    print("类方法")
# 静态方法
@staticmethod
def info():
    print("静态方法")
# 实例方法
def fun(self):
    print("实例方法")


P.tea1 = tea
P.info1 = info
# 实例名.实例方法名= types.MethodType(定义好的实例方法名, 实例)
per.fun1 = types.MethodType(fun, per)
P.tea1()
P.info1()
per.fun1()
