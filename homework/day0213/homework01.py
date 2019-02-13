from collections.abc import Iterable
from collections.abc import Iterator
# 使用yield得到生成器


def fun():
    yield 10
    yield 20
    yield 30
print(fun(), type(fun()))
a = fun()
print(next(a), next(a), next(a))

# 列表，元组，字典，字符串，整型
# 1.判断类型是否可以迭代
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({"name": "python1811"}, Iterable))
print(isinstance("python", Iterable))
print(isinstance(100, Iterable))

# 2.判断类型是否是迭代器
print(isinstance([1, 2, 3], Iterator))
print(isinstance((1, 2, 3), Iterator))
print(isinstance({"name": "python1811"}, Iterator))
print(isinstance("python", Iterator))
print(isinstance(100, Iterator))

# 如果是迭代器则使用next得到所有内容
g = (x for x in range(5))
print(g, type(g))
print(isinstance(g, Iterable), isinstance(g, Iterator))
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print(e)
        break
