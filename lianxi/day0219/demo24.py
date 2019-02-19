"""
Process进程下使用Queue队列共享数据
"""
from multiprocessing import Queue
from multiprocessing import Process
import time


# 向队列里取数据
def read(q):
    while True:
        time.sleep(1)
        print(q.get(block=False), q.qsize())


# 向队列里存数据
def write(q):
    for i in range(5):
        # time.sleep(1)
        q.put(i)


def main():
    # 队列
    q = Queue(5)
    q.put(-1)
    q.put(-2)
    # 进程
    pr = Process(target=read, args=(q, ))
    pw = Process(target=write, args=(q, ))
    pr.start()
    pw.start()

    pr.join()
    pw.join()
    print("finish")


if __name__ == '__main__':
    main()