"""
内建模块（类集合）  函数  属性
"""
"处理日志"
# import logging
# s1 = str(10)
# l2 = list(())
# g3 = iter([])
# print("++")
# logging.basicConfig(filename="log.log",filemode='a')
# logging.debug("debug..........")
# logging.error("error............")
# logging.warning("warning.........")

from collections.abc import Iterator
def fun(x):
    return x**x

"""
将可迭代对象的每一个参数均参与 fun函数运算
"""
# l2 = map(fun, [1,2,3])
# print(l2)
# print(isinstance(l2, Iterator))
# for r in l2:
#     print(r)


# def f(x):
#     return x>0

"""
将可迭代对象进行遍历，每一个元素均参与函数运算
"""
# l2 = filter(f, [-100,-50,0,10,50])
# print(l2)
# print(isinstance(l2, Iterator))
# for r in l2:
#     print(r)


from _functools import reduce

def fadd(x, y):
    return x+y

result = reduce(fadd, [1,2,3,4])
print(result)

# reversed()

class A():
    name = "zzy"
    def __init__(self):
        print("构造")
    def __del__(self):
        print("析构：回收时调用")
    def __str__(self):
        return "这是类A"
    def __repr__(self):
        return "这是类A的另一种描述胡"
a = A()

print(a)
