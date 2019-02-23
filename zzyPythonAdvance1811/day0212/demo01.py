"""
属性
类属性与实例属性
类与实例
类：使用class编写的代码模板
实例（对象）：类的构造方法的返回值（实例的引用）

属性：类中的字段
方法：操作属性的代码段


对比：
1,类属性只和类相关（属于类）
2,实例属性通常定义在构造函数中
3，类可以访问类属性，不可访问实例属性
    实例可以访问类属性， 可以访问实例属性

"""

class Person(object):
    "类属性"
    name = "pythonstu"
    def __init__(self, _age):
        "实例属性"
        self.age= _age

"通过构造函数得到类的实例"

# s1 = Person(1)
# s2 = Person(5)
# Person.name="zzy"
# print(s1.name , s2.name)

# s1 = Person(100)
# s2 = Person(200)

# print(s1.name, s2.name)
# s1.age=50
# print(s1.age, s2.age)
# "类不能访问实例属性"
# print(Person.age)



# TODO 明天上班了需要做一个实力属性和类属性的对比案例
