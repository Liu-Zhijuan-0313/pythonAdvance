# 进程通信，两个进程同时操作队列，有读有写
# 使用Queue共享数据，创建队列
from multiprocessing import Queue
from multiprocessing import Process
import time


# 向队列里放数据
def writep(q1):
    while True:
        q1.put(0)
        time.sleep(2)


# 一直等待队列里有数据
def readp(q1):
    while True:
        r = q1.get()
        print(r)


if __name__ == '__main__':
    q = Queue(5)
    q.put(-2)
    q.put(-1)
    pw = Process(target=writep, args=(q,))
    pr = Process(target=readp, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.join()
    print("finish")
