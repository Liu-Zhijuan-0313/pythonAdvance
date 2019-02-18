from multiprocessing import Pool
import time
import os


def processmain(index, **kwargs):
    time.sleep(1)
    print("pid %s 子进程 %s %s" % (os.getpid(), index, kwargs))


def main():
    pool = Pool(5)
    for i in range(10):
        # 非阻塞，五个一起开启
        # pool.apply_async(func=processmain, args=(i, ), kwds={"num": "i"})
        # 阻塞即for循环阻塞，一个一个的开启
        pool.apply(func=processmain, args=(i, ), kwds={"num": i})
    # 关闭进程池
    pool.close()
    # 如果没有join则子进程不运行,直接运行主进程
    # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭
    pool.join()
    print("finish")


if __name__ == '__main__':
    main()
