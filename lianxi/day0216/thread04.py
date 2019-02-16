# 多进程的应用程序
from multiprocessing import Process
# 多进程Process中实现数据共享
from multiprocessing import Queue
# 多进程池
from multiprocessing import Pool
# 多进程Pool中实现数据共享
from multiprocessing import Manager
# 多线程
import threading
import time
import os


def mainp(num, b, str, **kwargs):
    print("++")
    # 多进程外中获得id
    print(os.getpid())
    print(num, b, str, kwargs)


def maint():
    print("++")

def main():
    # 1.多进程
    # p1 = Process(target=mainp)
    # p1.start()
    # 多进程外面获得id
    # print(p1.pid)

    # 2.异步进程池开启一个函数的入口
    # 不需要start，
    pool = Pool(5)
    pool.apply_async(mainp, (10, True, "hello"), {"gender": "nv"})
    # 该进程池不再接受新的进程请求
    pool.close()
    # 等待该进程池结束以后才执行主程序
    # 主程序结束了，进程还没有结束，编辑器无输出
    # 不代表出错，可以执行下载图片等其他操作
    pool.join()

    # 3.多线程
    t1 = threading.Thread(target=maint)
    t1.start()

    # 4.如何使用队列在进程之间共享数据
    # 指定队列长度,put存数据，get拿数据
    # q = Queue(5)
    # q.put(1)
    # q.put_nowait()
    # q.get()
    # q.get_nowait()

    # 5.如何使用队列在进程池Pool之间共享数据
    q = Manager().Queue(5)
    print(type(q))


if __name__ == '__main__':
    main()