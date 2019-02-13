"""
isinstance()
python数据类型：int，float，boor,str,
可迭代：list,tuple,set,dict,generator
迭代器：generator（生成器是可迭代的也是迭代器）
可迭代：可以用for循环
迭代器：可以用next
iter()函数将可迭代的对象转换为迭代器
"""
from collections.abc import Iterable
a = (x for x in range(5))
print(a, type(a))
print(isinstance(a, Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({1, 2, 3}, Iterable))
print(isinstance({"name": "lzj"}, Iterable))

from collections.abc import Iterator
a = (x for x in range(5))
print(isinstance(a, Iterator))
print(isinstance([1, 2, 3], Iterator))
print(isinstance((1, 2, 3), Iterator))
print(isinstance({1, 2, 3}, Iterator))
print(isinstance({"name": "lzj"}, Iterator))

listA = [1, 2, 3]
print(isinstance(iter(listA), Iterator))
