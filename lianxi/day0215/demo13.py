# #TODO空格注释内容（在pycharm中左下角点击方便查看注释）
# 在提交git时会提示不完善，也可以提交
# TODO 执行函数的性能消耗
import time


def counttime(fun):
    def count():
        start = time.time()
        fun()
        end = time.time()
        print(fun.__name__, "耗时", end-start)
    return count

@counttime
def showlist():
    listA= [x for x in range(1000000)]
    for r in listA:
        print(r)
showlist()
