"""
threadlocal 线程独立副本 其他线程不能访问本线程的数据
"""
from threading import local,Thread
localvar = local()
# print(localvar, type(localvar))
localvar.name = "zzy"
print(localvar.name)


def fun1():
    print("begin")
    localvar.age=88
    print(localvar.name)
t1 = Thread(target=fun1)
t1.start()
t1.join()

print(localvar.age)