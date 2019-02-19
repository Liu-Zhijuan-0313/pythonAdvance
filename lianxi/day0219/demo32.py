"""
threadlocal线程独立副本，其他线程不能访问本线程的数据
因为多线程用的内存相同，如果一个线程改变了内存，其他线程内存跟着改变，
为了一个线程改变了内存，其他线程内存不改变，使用threadlocal
"""
from threading import Thread, local
l = local()
print(l)
l.name = "lzj"
print(l.name)


def fun():
    print("+++++")
    l.age = 20
    print(l.age)
    # 子线程访问不到主线程定义的name
    # print(l.name)


t = Thread(target=fun)
t.start()
t.join()
# 主线程访问不到子线程定义的age
# print(l.age)
