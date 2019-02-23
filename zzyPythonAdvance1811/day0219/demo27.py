"""
线程
多个线程之间执行没有固定的先后顺序需要抢占CPU资源
# 其实Python多线程伪多线程，本质并不是并行的，

"""
from threading import Thread
import time
def threadmain(name):
    while True:
        time.sleep(1)
        print(name,"执行了")

def main():
    thread1 = Thread(target=threadmain, args=("线程1",))
    thread2 = Thread(target=threadmain, args=("线程2",))
    thread1.start()
    thread2.start()
if __name__ == "__main__":
    main()