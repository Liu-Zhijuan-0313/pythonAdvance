"""
map函数会根据提供的函数对指定序列做 (映射)
reduce函数会对参数序列中元素进行 (累积)
filter函数会对指定序列执行 (过滤) 操作
"""

"""
1.map(function, iterable, ...)
    function -- 函数
    iterable -- 一个或多个序列
    返回迭代器。
2.reduce(function, iterable[, initializer])
    function -- 函数，有两个参数
    iterable -- 可迭代对象
    initializer -- 可选，初始参数
    返回函数计算结果
3.filter(function, iterable)
    function -- 判断函数。
    iterable -- 可迭代对象
    返回列表
"""
"1.map() 映射"
# from collections.abc import Iterator
#
#
# def fun(x):
#     return x**x
#
#
# "map(function函数，iterable)，将可迭代对象的每一个参数都参与fun函数运算"
# a = map(fun, [1, 2, 3])
# print(a)
# print(isinstance(a, Iterator))
# for i in a:
#     print(i)

"2.reduce() 累积"
# from _functools import reduce
#
#
# def fun2(x, y):
#     return x+y
#
#
# "将可迭代对象进行遍历，每一个元素均参与函数运算"
# "1+2=3, 3+3=6,6+4=10,10+....."
# a2 = reduce(fun2, [1, 2, 3, 4])
# print(a2)

"3.filter()过滤"
# def fun3(x):
#     return x % 2 != 0
#
#
# a3 = filter(fun3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a3, type(a3))
# for i in a3:
#     print(i)

