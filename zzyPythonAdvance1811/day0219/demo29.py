"""
多线程共享全部对象产生问题
GIL锁：全局解释锁
互斥锁：资源互斥锁：线程想要访问某个资源前需要给资源加锁，加锁成功，就可以方法
加锁失败，需要陷入等待，直到加锁成功
"""
from threading import  Thread, Lock
# 得到一把锁
lock = Lock()
num = 0
def fun():

    global num
    for r in range(1000000):
        # 使用资源需要加锁
        lock.acquire()
        num = num+1
        #  使用完毕解锁
        lock.release()


t1 = Thread(target=fun)
t1.start()


# print(num)
t2 = Thread(target=fun)
t2.start()

t1.join()
t2.join()
print(num)

# num 1
# num 99+1

"""
多进程：内存独立，需要共享数据就是用queue
多线程：内存不独立，本身就共享数据但是会产生线程不安全数据

"""