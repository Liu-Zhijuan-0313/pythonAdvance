"""
Process进程封装类
"""
from multiprocessing import Process
import os


def fun():
    print("aaa")


class MyProcess(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        super().__init__(group, target, name, args, kwargs)

    def run(self):
        print("进程启用了", os.getpid())


p1 = MyProcess(name="进程A", target=fun)
p1.run()

"""
1.使用系统进程类 Process则不需要重写run方法， 通过给target定义进程入口函数
2.使用自定类继承 Process类 重写run方法 进程启动后会执行run方法
"""