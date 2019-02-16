# 进程通信，两个进程同时操作队列，有读有写
# 进程池下共享Queue，使用Manager创建队列
from multiprocessing import Pool
from multiprocessing import Manager
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
    q = Manager().Queue(5)
    q.put(-2)
    q.put(-1)

    pool = Pool(5)
    pool.apply_async(writep, (q,))
    pool.apply_async(readp, (q,))
    pool.close()
    pool.join()
    print("finish")
