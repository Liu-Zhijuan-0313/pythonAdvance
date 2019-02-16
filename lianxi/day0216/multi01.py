# 1.子进程返回0
# 父进程返回子进程的id
# getpid()当前进程、getppid()当前进程的父进程

# from multiprocessing import Process
# import os
# print(os.getpid())
#
#
# def fun():
#     print("子进程", os.getpid(), os.getppid())
#
#
# if __name__ == '__main__':
#     print("创建子进程后")
#     p = Process(target=fun)
#     p.start()
#     p.join()
#     print("+++")


# from multiprocessing import Process
# import os
# def fun():
#     print("child pid %d" % os.getpid())
# print("parent pid %d" % os.getpid())
# p = Process(target=fun)
# if __name__ == '__main__':
#     print("has not exec")
#     p.start()
#     p.join()
#     print("exec finish")

# 2.带参数的进程
from multiprocessing import Process
import os
import time


def childmain(name, age, **kwargs11):
    print("子进程", os.getpid())
    print(name, age, kwargs11)


def main():
    print("主进程", os.getpid())
    p = Process(name="child", target=childmain, args=("lzj", 20), kwargs={"isalive": False})

    # is_alive()判断子进程是否存活
    # name 起别名
    print(p.is_alive(), p.name)

    p.start()
    # terminate()终止子进程
    # p.terminate()
    time.sleep(1)

    # join()阻塞子进程
    # p.join()
    print(p.is_alive())
    print("+++++")


if __name__ == '__main__':
    main()



