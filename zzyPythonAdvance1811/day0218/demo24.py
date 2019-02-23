"""
使用Queue完成多进程共享数据（共享队列中数据）
"""
from multiprocessing import Queue,Process
import time

def read(q):
    while True:
        time.sleep(1)
        print("队列中取出数据",q.get())
def write(q):
    for i in range(1000):
        q.put(i)


if __name__ == "__main__":
    q = Queue(5)
    q.put(-2)
    q.put(-1)
    pr = Process( target=read, args=(q,))
    pw = Process( target=write, args=(q,))
    pr.start()
    pw.start()
    pr.join()
    pw.join()
    print("主进程执行完毕")

#程序执行后q 放入-2 -1
# 写进程放入 0 1 2 此时队列中有 -2 -1 0 1 2
# 读进程一秒之后取出 -2 此时队列中有 -1 0 1 2 写进程可以写入3
# 读进程一秒之后取出 -1 此时队列中有  0 1 2 3 写进程可以写入4
