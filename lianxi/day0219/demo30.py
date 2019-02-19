"""
多线程-封装
"""
from threading import Thread
from typing import Optional, Callable, Any, Iterable, Mapping


class ThreadPro(Thread):

    def __init__(self, name1):
        Thread.__init__(self, name=name1)

    def run(self):
        print("线程启动了")


t = ThreadPro("lzj")
t.start()
# name是继承过来的属性
print(t.name)