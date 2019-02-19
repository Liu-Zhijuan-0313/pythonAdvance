"""
在函数内部赋值的局部变量，global不能访问到
多个线程可以共享主线程数据
"""
from threading import Thread
num = 10


def threadmain():
    global num
    num = 20
    print("子线程", num, id(num))


def main():
    t = Thread(target=threadmain)
    t.start()
    t.join()
    print("主线程", num, id(num))


if __name__ == '__main__':
    main()