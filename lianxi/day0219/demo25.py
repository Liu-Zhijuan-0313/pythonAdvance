""""
Pool进程池下使用Manager队列实现数据共享
"""
from multiprocessing import Manager
from multiprocessing import Pool
import time


# 向队列里取数据
def read(q):
    while True:
        time.sleep(2)
        print("取数据值%s,剩余大小%s" % (q.get(), q.qsize()))


# 向队列里存数据
def write(q):
    while True:
        time.sleep(1)
        q.put(0)


def main():
    # 队列
    q = Manager().Queue(100)
    # 异步非阻塞进程池
    pool = Pool(5)
    pool.apply_async(func=read, args=(q, ))
    pool.apply_async(func=write, args=(q, ))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()