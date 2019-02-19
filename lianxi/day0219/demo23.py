"""
队列：Queue
    可以用来实现进程之间共享数据
"""
from multiprocessing import Queue
q = Queue(3)
# 队列的大小
print(q.qsize())
# 队列是否满了
print(q.full())
q.put(1)
q.put(2)
q.put(3)
print(q.qsize())
print(q.full())
try:
    q.put(4, block=True, timeout=1)
    q.put_nowait(5)
except Exception as e:
    print(e)
# 从队列里取数据，原则：先进先出
print(q.get())
print(q.get())
print(q.get())
print(q.qsize())
# 是否为空队列
print(q.empty())