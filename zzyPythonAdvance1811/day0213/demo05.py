"""
生成器第一种实现
"""

"列表生成式 很好用，但是有缺点，有多少个元素就需要开辟多的空间 "
# l1 = [x for x in range(100000)]
# print(l1[100])
"生成器写法 对象多占内存跟元素个数无关"
"生成器不能使用下标,但是可以使用for循环和 next（生成器对象）"
"生成器后面数据根据前面数据推算出来"
""
# l2 = (x for x in range(100000))
# print(next(l2),next(l2),next(l2),next(l2))
# print(l1.__sizeof__())
# print(l2.__sizeof__())

# for r in l1:
#     print(r)

# for r in l2:
#     print(r)



"""
生成器第二种写法，常见一种函数写法
通过函数 + yield
函数的内部有yield 函数返回的为生成器
yield 向生成器内部放入对象
如果要获取函数的原始返回值，需要通过next访问所有对象（出错了，错误异常即函数原始返回值）
"""

# def fun():
#     yield 10
#     yield 20
#     yield 30
#     return "helloworld"
#
# result = fun()
# print(type(result))
# for r in result:
#     print(r)

# print(next(result))
# print(next(result))
# print(next(result))
#
# try:
#     print(next(result))
# except StopIteration as e:
#     print(e)


"""
裴波拉契算法  从第三项起每一项为前两项的和  
0 1 1 2 3 5 8 ...
"""

# a, b = 0, 1
# print(a, b)
# a, b = b, a+b
# print(a, b)
# a, b = b, a+b
# print(a, b)
# a, b = b, a+b
# print(a, b)

def fun(n):
    a, b = 0, 1
    yield a
    yield b
    count = 0
    while count<n:
        a, b = b, a + b
        yield b
        count += 1
    return "Finish"


result = fun(30)
# for r in result:
#     print(r)

while True:
    try:
        print(next(result))
    except StopIteration as e:
        print("next方法出现异常,原因",e)
        break
