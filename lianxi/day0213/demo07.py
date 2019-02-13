"""
闭包:
    1.函数内部嵌套函数
    2.内部函数可以访问外部函数局部变量，并且保存变量
    3.外部函数将内部函数返回
因为外部函数返回的为内部函数的引用
外部函数每执行一次都要返回内部函数的引用（该引用保存了外部函数的局部变量）
"""


def fun1():
    a = 1

    def fun2(b):
        return a + b
    return fun2


print(fun1, type(fun1))
print(fun1(), type(fun1()))
print(fun1()(2))

r1 = fun1()
print(r1(10))
r2 = fun1()
print(r2(20))
