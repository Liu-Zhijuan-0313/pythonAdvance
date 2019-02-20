import threading
import time
num = 1

# 1.
# def fun1():
#     global num
#     num = 2
# fun1()
# print(num)


# 2.
def fun3():
    global num
    num = 4


t1 = threading.Thread(target=fun3)
t1.start()
time.sleep(1)
print(num)
