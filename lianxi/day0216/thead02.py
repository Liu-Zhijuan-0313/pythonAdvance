# 1.封装线程类,无run方法，可以执行threadfun打印+++
# import threading
#
#
# class MyThread(threading.Thread):
#     pass
#
#
# def threadfun():
#     print("+++")
#
#
# t1 = MyThread(target=threadfun)
# t1.start()

# 2.封装线程类，有run方法，不能执行threadfun打印+++，
# 实现统计时间
import threading


class MyThread(threading.Thread):
    def run(self):
        print("--")

    def counttime(self):
        pass


def threadfun():
    print("+++")


t1 = MyThread(target=threadfun)
t1.start()
t1.counttime()