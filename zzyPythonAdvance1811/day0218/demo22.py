"""
进程池：池子中用来存放可用进程
需要初始化池子中存储进程数

apply_async 非阻塞 一个进程开启后另外进程随便开启
apply阻塞
"""
from multiprocessing import Pool
import os
import time
def processmain(index, **kw):
    time.sleep(1)
    print("进程",os.getpid(), "当前循环为", index, kw )

if __name__ == "__main__":
    pool = Pool(5)
    for i in range(100):
        "非阻塞 只要池子中有可用进程则开始"
        # pool.apply_async(func=processmain, args=(i,),kwds={"num": i})

        pool.apply(func=processmain, args=(i,),kwds={"num": i})
    pool.close()
    pool.join()
    print("finish")