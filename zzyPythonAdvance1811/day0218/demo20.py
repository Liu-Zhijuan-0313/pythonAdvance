"""
Python 是跨平台语言
Windows开发项目
Linux部署项目
fork不能用 可使用mulprocess
"""
import os
from multiprocessing import Process
# print(Process.__dict__)
import time
def processA(a, b, c, **kwargs):
    print(a, b, c, kwargs)
    time.sleep(2)
    print(" 进程A执行了， 进程id为", os.getpid())

def main():
    print("主进程id", os.getpid())

    # run方法为进程定义的入口方法 开启进程 执行run方法
    # run方法可以被重写
    # 或者使用target参数定义进程入口函数
    p1 = Process(name="进程A", target=processA, args=(4,5,6), kwargs= {"name": "zzy"})
    p1.start()
    # join方法能够阻塞主进程， print(p1.name)陷入等待 等待p1进程执行完毕
    print(p1.is_alive())

    # terminate  结束进程
    # p1.terminate()
    p1.join()
    print(p1.name)
    print(p1.is_alive(),p1.pid)

if __name__ == "__main__":
    main()