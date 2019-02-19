"""
多线程共享全部对象产生问题
GIL锁：全局解释锁
资源互斥锁：线程想要访问某个资源之前需要给资源加锁，
加锁成功就可以访问，失败需要陷入等待，直到加锁成功
"""
"""
多进程：内存独立，需要共享数据用Queue
多线程：内存不独立，本身就共享数据但是会产生线程不安全数据
"""
from threading import Thread, Lock

lock = Lock()
num = 0


def fun():
    global num
    for i in range(1000000):
        # 需要使用num资源加锁
        lock.acquire()
        num += 1
        # 使用完解锁
        lock.release()


def main():
    t1 = Thread(target=fun)
    t2 = Thread(target=fun)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(num)


if __name__ == '__main__':
    main()

"""
1.GIL不是Python特性
    GIL是Python解释器（Cpython）时引入的概念，在JPython、PyPy中没有GIL。GIL并不是Python的语言缺陷。
2.GIL定义
    GIL，the Global Interpreter Lock，直译为“全局解释锁”
3.GIL存在原因
    CPython在执行多线程的时候并不是线程安全的，所以为了程序的稳定性，加一把全局解释锁，能够确保任何时候都只有一个Python线程执行。
4.GIL的弊端

    GIL对计算密集型的程序会产生影响。因为计算密集型的程序，需要占用系统资源。GIL的存在，相当于始终在进行单线程运算，这样自然就慢了。

    IO密集型影响不大的原因在于，IO，input/output，这两个词就表明程序的瓶颈在于输入所耗费的时间，线程大部分时间在等待，所以它们是多个一起等（多线程）还是单个等（单线程）无所谓的。
    这就好比，你在公交站等公交时，你们排队等公交（单线程）还是沿着马路一字排开等（多线程）是无所谓的。公交车（即input，即输入的资源）没来，哪种方式都是瞎折腾。


5.解决方案
    (1) multiprocessing
    multiprocessing是一个多进程模块，开多个进程，每个进程都带一个GIL，就相当于多线程来用了。

    (2) multiprocessing的弊端
    多线程与多进程一个不同点在于：
    ***多线程是共享内存的，即这些线程共用一个内存地址。好处在于便于线程间数据通信和数据同步。
    ***多进程，各个进程地址之间是独立的内存地址。这样不存内存地址之间通信就麻烦了。
        如果是IO密集型且对数据通信有需求，使用python 的threading模块也是可以的。
"""
