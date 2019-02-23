from threading import  Thread

class ThreadPro(Thread):
    def __init__(self, na= None):
        Thread.__init__(self,name=na)

    def run(self):
        print("线程启动了")

t1 = ThreadPro(na="t11")
t1.start()
print(t1.name)