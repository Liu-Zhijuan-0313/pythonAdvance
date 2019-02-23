"""
2，新建2.py文件编码验证迭代器与可迭代的区别
"""
# 1.可迭代对象:可以使用for...in...语句进行循环的对象，
# 比如字符串、列表、元组、字典以及迭代器、生成器都是可迭代对象。
# 可以使用isintance()来判断
# 2.迭代器:可以使用next()进行回调的对象，
# 可迭代对象和迭代器的联系是：可以对迭代对象使用iter()方法来生成迭代器。
from collections.abc import Iterable, Iterator
listA = [1, 2, 3]
print(isinstance(listA, Iterable))
print(isinstance(listA, Iterator))
listA = iter(listA)
print(isinstance(listA, Iterator))