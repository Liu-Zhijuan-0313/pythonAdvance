"""
6，封装进程类MyProcess
要求进程执行后输出“（进程名..执行了）”
"""


class MyProcess:
    def __init__(self):
        print(MyProcess.__name__)

    def run(self):
        print("%s进程，执行了" % (MyProcess.__name__, ))


p = MyProcess()
p.run()
