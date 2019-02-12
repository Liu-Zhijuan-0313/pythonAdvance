"""
类属性不会因实例不同而不同
实例属性通常需要类__init__方法初始化
实例可以调类属性、类不可以调实例属性
"""


class Person:
    # 类属性
    name = "python1811"

    def __init__(self, age):
        # 实例属性
        self.age = age


# a1, a2为实例
a1 = Person(20)
a2 = Person(30)
# 实例可以访问类属性，实例属性
print(a1.name, a2.name)
print(a1.age, a2.age)
# a1.name = "python"
a1.age = 25
print(a1.name, a2.name)
print(a1.age, a2.age)
Person.name = "lzj"
print(a1.name, a2.name)
