from multiprocessing import Process

def processmain():
    print("process main")

class ProcessPro(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        super().__init__(group, target, name, args, kwargs)
    def run(self):
        print("进程启用了")

if __name__ == "__main__":
    p1 = ProcessPro(name="p1")
    p1.start()
    print(p1.name)
"""
1使用系统进程类 Process则不需要重写run方法， 通过给target定义进程入口函数
2使用自定类继承 Process类 重写run方法 进程启动后会执行run方法
"""