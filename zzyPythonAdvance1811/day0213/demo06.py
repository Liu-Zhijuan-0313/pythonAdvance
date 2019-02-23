"""
生成器：为了节省内存空间才是用可以生成 数列 类型为genertor
迭代器Iterator：可以使用next就是迭代器
可迭代Iterable：可以使用for循环
isinstance方法可以用来判断对象是否是某各类的实例 True代表是该类实例


生成器可迭代
可迭代不一定是迭代器
迭代器一定是可迭代的
"""
"""
Python有哪些数据类型
int bool float None  不可迭代
str list turple dict set  
generator 可迭代类型 也是生成器

"""


from collections.abc import Iterable,Iterator

"1 如何判断是否可以迭代"
# g = (x for x in range(10))
# print(type(g))
# for r in g:
#     print(r)
# print( isinstance("", Iterable)  )

"2 如何判断是否为迭代器"
l = [x for x in range(10)]
g = (x for x in range(10))
# print(next(g))
# print(isinstance({5,6}, Iterator))
g2 = iter(l)
print(next(g2))
print(type(g2))
print(isinstance(g2,Iterator))


