# 多线程下载
# 封装具有下载图片功能的线程
import threading
import requests


class DownLoadImg(threading.Thread):
    def __init__(self, _url):
        # 初始化父类的构造，说明才是一个完整的线程
        threading.Thread.__init__(self)
        self.url = _url

    def run(self):
        # 下载图片
        imgcontent = requests.get(self.url).content
        with open("d:/op.jpg", "wb") as f:
            f.write(imgcontent)


t = DownLoadImg("https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/86770226")
t.start()
