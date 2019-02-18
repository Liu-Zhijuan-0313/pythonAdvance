"""
编写完毕的代码,在没有运行的时候，称为程序
正在运行着的代码,称为进程
进程除了包含代码之外还要有代码的运行环境
"""
from multiprocessing import Process
import os
import time


def fun(a, b, **kwargs):
    print(a, b, kwargs)
    time.sleep(2)
    print("子进程开始运行了 pid", os.getpid())
    time.sleep(2)


def main():
    p1 = Process(name="进程A", target=fun, args=(1, "hello"), kwargs={"name": "lzj"})
    print("主进程%s开始运行了 pid%s" % (p1.name, os.getpid()))
    # 启动p1
    p1.start()
    # 终止子进程的运行
    # p1.terminate()
    # 阻塞主进程，等待子进程结束后再执行
    p1.join()
    print(p1.pid)
    print("完成")


if __name__ == '__main__':
    main()
