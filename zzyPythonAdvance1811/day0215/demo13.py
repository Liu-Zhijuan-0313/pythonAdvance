"""
统计性能装饰器
"""
import time
def cost(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, "耗时",str(end-start))

        pass
    return fun

# TODO fun1方法使用了列表存储 等我学会生成器之后需要改成生成器的写法
@cost
def fun1():
    l = [x for x in range(1000000)]
    for r in l:
        print(r)
@cost
def fun2():
    g = (x for x in range(1000000))
    # print(g.__sizeof__())
    for r in g:
        print(r)


# fun1()
fun2()

"""
TODO 注释
需要完善的地方
"""