import threading
import socket


# TCP客服端发消息
def sendinfo():
    while True:
        # 如果客户端输入exit发给服务器，表示要关闭客户端
        data1 = input("请输入发送到服务端的内容：")
        if data1 == "exit":
            client.close()
        else:
            client.send(data1.encode("gbk"))


# TCP客服端接受消息
def recvinfo():
    while True:
        databytes = client.recv(1024)
        # 如果服务器断开了客户端，会一直发送空字符串，
        # 所以判断收到空字符串，客户端要关闭
        if len(databytes) == 0:
            client.close()
            break
        else:
            datastr = databytes.decode("gbk")
            print("从服务器接受到的数据：", datastr)


if __name__ == '__main__':
    try:

        # 1.创建TCP客户端对象
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.和服务器建立连接
        client.connect(("192.168.15.40", 6666))

        # 3.第一次发送的内容，为客服端的名字
        clientnamestr = input("请输入客户端的名字：")
        clientnamebytes = clientnamestr.encode("gbk")
        client.send(clientnamebytes)

        # 4.创建客户端收发消息两个线程
        sendt = threading.Thread(target=sendinfo)
        recvt = threading.Thread(target=recvinfo)
        sendt.start()
        recvt.start()
    except Exception as e:
        print(e)

