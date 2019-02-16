# 队列
from multiprocessing import Queue
q = Queue(3)
q.put(1)
q.put(2)
q.put(3)

print(q.qsize())

# #  队列满了设置False，直接报错
# q.put(4, False)
# q.put_nowait(4)
# # 队列满了True则等待2秒之后报错
# q.put(4, True, 2)
# print(q.qsize())

# 队列先进先出
print(q.get())
print(q.get())
print(q.get())

# 队列满了设置False，直接报错
# 队列满了True则等待2秒之后报错
print(q.get(True, 2))
