"""
Python一切皆对象
类Person：创建对象p1
类Person也是一个对象
元类：创建类Person
元类：创建元类

type 创建了type
type 创建了 Person类（对象）
Person类创建了p1对象

"""
# class Person():
#     def __init__(self, _name):
#         self.name = _name
#
# p1 = Person("zzy")
# print(type(p1),  p1.__class__)
# print(type(Person), Person.__class__)
# print(type(type),type.__class__)

"使用type类创建Person"
# 第一个参数 为类名字符串 第二个参数为 父类元组 ， 第三个参数为该类的属性字典格式
Ps = type("Person", (), {"name": "zzy", "age": 20})
# print(type(Ps), Ps.__class__)
# print(Ps.__name__)
St = type("Student", (Ps,), {"stdnum": 1001})
print(type(St))
print(St.__bases__, Ps.__bases__)
# print(hasattr(St,"name"))
s1 = St()
print(s1.name,s1.stdnum)
St.score = 100
print(s1.score)

"动态的添加 类方法  静态方法 实例方法"

@classmethod
def sleep(cls):
    print(cls)

@staticmethod
def eat():
    print("eat")

def study(self):
    print("好好学习，不睡觉")

Human = type("Human", (), {"sleep1": sleep, "eat1": eat, "study1": study })

wzk = Human()
wzk.study1()
Human.sleep1()
Human.eat1()
