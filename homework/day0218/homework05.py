"""
fork只能在Linux上运行
子进程fork方法的返回0，父进程fork方法的返回子进程的pid
当前进程：os.getpid()
当前进程的父进程：os.getppid()
"""
# 1.在Linux的进程
# import os
# print(os.getpid())
# pid = os.fork()
# if pid == 0:
#     print("子进程id %s, 父进程id %s" % (os.getpid(), os.getppid()))
# else:
#     print("父进程id %s, 子进程id %s" % (os.getpid(), os.getppid()))


# 2.在Window的进程
from multiprocessing import Process
import os
import time
time.sleep(3)
print("当前进程id", os.getpid())


def fun(a, b, **kw):
    print(a, b, kw)
    time.sleep(5)
    print("当前子进程id", os.getpid(), "父进程id", os.getppid())
    time.sleep(5)


def main():
    print("当前父进程id", os.getpid(), "当前进程的父进程id", os.getppid())
    p = Process(target=fun, name="Function", args=(1, "hello"), kwargs={"name": "lzj"})
    print("进程别名", p.name)
    p.start()
    # 终止子进程
    # p.terminate()
    # 阻塞主进程，等待子进程运行完再执行主进程
    p.join()
    print("finish")


if __name__ == '__main__':
    main()
