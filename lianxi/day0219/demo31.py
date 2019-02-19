"""
互斥锁的使用：
加锁成功，失败就等待
只能加一次锁，两次会失败，因为加过了
"""
from threading import Lock
# 得到锁的对象
lock = Lock()
num = 10
# 访问资源前加锁
lock.acquire()
num = 20
# 使用完毕解锁
lock.release()
print(num)