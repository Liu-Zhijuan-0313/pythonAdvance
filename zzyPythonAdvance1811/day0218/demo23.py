"""
多进程：
进程:一个运行的程序
os.fork() windows不支持
可以开启子进程
fork方法执行一次会有两个返回值
为0时代表当前执行进程为子进程
不为0时代表当前创建子进程的pid
os.getpid()
os.getppid()
跨平台：window平台，linux部署 同一套代码
from multiprocessing import Process
def __init__(name= ,target=,args=,kwargs=)
p1 = Process()
p1.name
p1.pid
p1.start()
p1.terminate()
p1.join()
阻塞与非阻塞
阻塞（影响后续代码执行）
非阻塞（不影响后续代码执行）
def run()
    pass
Process
当run方法没有重写 进程启动之后可以执行target指定的入口函数
如果run方法在子类被重写，子类创建的进程开启时会执行重写的run方法
进程池概念
开辟池子存储可用进程：当需要时从进程池取，不需要时放入进程池
避免内存的返回申请与回收
from multiprocessing import Pool
pool = Pool(10)
池子中默认存放10个可用进程（需要10个内存空间）
需求：取100个进程
因为本省只有10进程
applay(target=， args= ,kwds=, )：从池子取一个进程，在该进程执行完之前不能继续取，必须等待进程执行完毕
applay_async(异步非阻塞)：可以连续从池子取进程，直到把池子取空，继续取时需要等待之前进程执行完毕

进程之间可以传参 args  kwargs


"""
# from multiprocessing import Pool
# import time
# def processmain(num,l222):
#     time.sleep(2)
#     print("begin",num, l222)
#     num = 200
#     l222[3].append(4.5)
#     print("子进程执行完毕，子进程中list值为",l222)
#
# if __name__ == "__main__":
#     num = 100
#     l2 = [1,2,3,[4,5]]
#     pool = Pool(5)
#     pool.apply_async(processmain, args=(num,l2))
#     pool.close()
#     pool.join()
#     print("finish")
#     print("主进程执行完毕，l2值为",l2)
#  两个进程之间数据相互独立， 相当于操作系统给两个进程都分配了独立的内存
#  子进程会拷贝主进程数据放入独立的内存空间 相当于深拷贝 deepcopy
#  进程之间如何共享数据
# 为何要共享数据：高并发
# 单进程情况处理十万个非常复杂的操作 需要10小时
#  如果开十个进程则每个进程需要处理一万条 需要一个小时
# 开的十个进程工作不能重复，进程之间需要共享数据
# 可以将十万条数据放入队列（Queue）
# 每一个进程都从队列取一万条
# 进程之间共享数据可以采用队列形式



from multiprocessing import Queue,ProcessError
q = Queue(3)
# print(q.qsize())
print(q.empty())
q.put(1)
q.put(2)
q.put(3)
print(q.qsize())
print(q.full())
# 如果不能放入只等待5秒钟
# q.put(4,block=True, timeout=5)

# try:
#     q.put_nowait(4)
# except Exception as e:
#     print(e)
# 数据结构队列先进先出
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.qsize())
print(q.full())

print("finish")



