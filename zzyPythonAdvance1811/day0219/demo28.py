from threading import Thread

def threadmain():
    global num
    num=20
    # print()
    print("子线程", num ,id(num))




if __name__ == "__main__":
    num = 10
    thread = Thread(target=threadmain)
    thread.start()
    thread.join()
    print("finish")
    print("主线程", num, id(num))


# 在函数内部赋值的局部变量 不能使用global访问到
# 多个线程可以共享主线程数据
#  