from multiprocessing import Pool,Manager
import time
import os
def read(q):
    print("读进程pid", os.getpid())
    while True:
        time.sleep(2)
        r = q.get()
        print("取到",r,"剩余",q.qsize())
def write(q):
    print("写进程pid", os.getpid())
    # l2 = []
    while True:
        time.sleep(1)
        # for r in range(100):
        #     l2.append(r)
        q.put(0)


if __name__ == "__main__":
    s = input("++")
    q = Manager().Queue(5000)
    pool = Pool(4)
    pool.apply_async(func=read, args=(q,))
    pool.apply_async(func=write, args=(q,))
    pool.close()
    pool.join()
    print("finish")
