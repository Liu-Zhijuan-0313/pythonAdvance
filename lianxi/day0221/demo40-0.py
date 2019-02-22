"""
TCP-多人聊天客户端
"""
import socket
from threading import Thread


def recvinfo():
    while True:
        databytes = clientSocket.recv(1204)
        if len(databytes) == 0:
            clientSocket.close()
            break
        else:
            datastr = databytes.decode("gbk")
            print("收到消息：", datastr)


def sendinfo():
    while True:
        try:
            if clientSocket._closed:
                break
            else:
                tousername = input("请输入向那个用户发送：")
                datastr = input("请输入发送内容：")
                datastr = tousername + "|" + datastr
                databytes = datastr.encode("gbk")
                clientSocket.send(databytes)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 创建客户端对象
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 客户端和服务器建立连接
    IP = ("192.168.15.40", 6666)
    clientSocket.connect(IP)

    # 用户名
    sendnamestr = input("用户名：")
    sendnamebytes = sendnamestr.encode("gbk")
    clientSocket.send(sendnamebytes)

    # 收发消息两个线程
    recvt = Thread(target=recvinfo)
    recvt.start()
    readt = Thread(target=sendinfo)
    readt.start()
