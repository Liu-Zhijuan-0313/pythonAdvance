import threading
import socket


def sendinfo():
    while True:
        data1 = input("请输入发送到服务端的内容：")
        if data1 == "exit":
            client.close()
        else:
            client.send(data1.encode("utf-8"))


def recvinfo():
    while True:
        databytes = client.recv(1024)
        if len(databytes) == 0:
            client.close()
            break
        else:
            datastr = databytes.decode("gbk")
            print("从服务器接受到的数据：", datastr.decode("utf-8"))


if __name__ == '__main__':
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("192.168.15.40", 6666))

        clientnamestr = input("请输入客户端的名字：")
        clientnamebytes = clientnamestr.encode("gbk")
        client.send(clientnamebytes)

        t1 = threading.Thread(target=sendinfo)
        t2 = threading.Thread(target=recvinfo)
        t1.start()
        t2.start()
    except Exception as e:
        print(e)

