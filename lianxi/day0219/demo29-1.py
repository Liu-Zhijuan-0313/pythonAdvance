"""
互斥锁:加锁目的防止数据不一致或丢失，
      加锁成功m1.acquire()返回True
"""
import threading
import time
num = 0


def fun1():
    global num
    for i in range(1000000):
        m.acquire()
        num += 1
        m.release()


def fun2():
    global num
    for i in range(1000000):
        # 需要使用资源num并修改则加锁
        m.acquire()
        num += 1
        # 使用完加锁
        m.release()


m = threading.Lock()
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()


# 需要等到子线程运行完执行主线程，
# 用join阻塞或者sleep睡眠阻塞主线程
# t1.join()
# t2.join()
time.sleep(2)
print(num)

"""
死锁:
    由于可以存在多个锁，不同的线程持有不同的锁，
    并试图获取对方持有的锁时，可能会造成死锁
"""
# import threading
# import time
#
#
# def fun1():
#     if m1.acquire():
#         time.sleep(1)
#         if m2.acquire():
#             print("finish1")
#
#
# def fun2():
#     if m2.acquire():
#         time.sleep(1)
#         if m1.acquire():
#             print("finish2")
#
#
# m1 = threading.Lock()
# m2 = threading.Lock()
# t1 = threading.Thread(target=fun1)
# t2 = threading.Thread(target=fun2)
# t1.start()
# t2.start()
