# import time
# import threading
#
# def sayhi():
#     print("hi")
#     time.sleep(1)


# start = time.time()
# for i in range(5):
#     sayhi()
# end = time.time()
# print(end - start)

# 2.单个线程
# import time
# import threading
#
# def sayhi():
#     time.sleep(1)
#     print("hi")
# def threamain():
#     print("++")
#
#
# t1 = threading.Thread(target=sayhi)
# t1.start()

# 3.多个线程
# 获取当前线程数量threading.enumerate()
import time
import threading


def sayhi():
    time.sleep(1)
    print("hi")


print(threading.enumerate())

start = time.time()
for i in range(5):
    t1 = threading.Thread(target=sayhi)
    t1.start()
    print(threading.enumerate())

end = time.time()
print(end-start)