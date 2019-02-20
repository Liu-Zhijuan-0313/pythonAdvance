""""
多线程
"""
# 1.在单进程单线程情况下 开启5次下载耗时操作需要5秒钟
import time
from threading import Thread


def prt():
    "模拟耗时操作 比如下载资源"
    time.sleep(1)
    print("+")


def singlethread():
    "单线程情况耗时"
    start = time.time()
    for r in range(5):
        prt()
    end = time.time()
    print("时间消耗", end - start)

# 2.在单进程 5个线程情况下 开启5次下载 应为线程是并发 所以只需要一秒钟就可已


def threadmain():
    prt()


def multithread():
    threadlist = []
    # 创建线程
    start = time.time()
    for r in range(5):
        t1 = Thread(name="线程"+str(r), target=threadmain)
        t1.start()
        threadlist.append(t1)
        print(t1.name)


    # 主线程执行完毕 子线程还没有执行完
    # 如果想要统计时间消耗 需要等待5个子线程执行完毕
    # 确保每个子线程都join才能统计结束时间
    # 阻塞主进程（需要的子线程都已经 创建成功）
    for t in threadlist:
        t.join()
    end = time.time()
    print("多线程耗时",end-start)


if __name__ == "__main__":
    # singlethread()
    multithread()

# 结果
# 在单进程单线程情况下 开启5次下载耗时操作需要5秒钟
# 在单进程 5个线程情况下 开启5次下载 应为线程是并发 所以只需要一秒钟就可已完成