"""
线程：
    多个线程之间执行没有固定的先后顺序需要抢占CPU资源
    其实python线程为多线程，本质不是并行的
"""
from threading import Thread
import time


def fun(name):
    print("start")
    while True:
        time.sleep(1)
        print(name, "执行了")


def main():
    thread1 = Thread(target=fun, args=("线程1", ))
    thread2 = Thread(target=fun, args=("线程2",))
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    main()
