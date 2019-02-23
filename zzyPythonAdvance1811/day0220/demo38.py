"""
TCP客户端
多线程
"""
import socket
from threading import Thread

def sendThread():
    while True:
        sendstr = input("请输入发送内容")
        if sendstr=="exit":
            client.close()
            break
        else:
            sendbytes = sendstr.encode("utf-8")
            client.send(sendbytes)

def recvThread():
    while True:
        if client._closed:
            databytes = client.recv(1024*1024)
            datastr = databytes.decode("utf-8")
            print("收到",datastr)
        else:
            break


if __name__ == "__main__":
    try:
        # 1创建套接字对象
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2连接服务器
        SERRVERADDR = ("192.168.15.3", 9999)
        client.connect(SERRVERADDR)
        # 添加用户系统
        # username = input("请输入用户名")
        # client.send(username.encode("utf-8"))
        # 3创建线程用来发送数据
        tsend = Thread(target=sendThread)
        tsend.start()
        trecv = Thread(target=recvThread)
        trecv.start()
    except Exception as  e:
        print("错误了", e)