import socket
import threading


def recvinfo(client1, data):
    while True:
        recvdata = client1.recv(1024)
        recvdatabytes = recvdata.decode("utf-8")
        print("收到客户端%s发送的内容:%s" % (data, recvdatabytes))
        if len(clientA) == 0:
            clientA.append((recvdatabytes, client1))
            print(clientA)
        else:
            a = False
            for i in clientA:
                if client1 == i[1]:
                    a=True
            if a==False:
                clientA.append((recvdatabytes, client1))
                print(clientA)


def sendinfo():
    while True:
        clientname2 = input("请输入发送数据的客户端名字：")
        senddata = input("请输入发送到客户端的内容：")
        senddatabytes = senddata.encode("utf-8")
        for i in clientA:
            if i[0] == clientname2:
                i[1].send(senddatabytes)


def acceptThead():
    while True:
        client, data = server.accept()
        print(client)
        print(data)
        print("客户端%s成功连接到服务器" % (data, ))
        recv1 = threading.Thread(target=recvinfo, args=(client, data))
        recv1.start()


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.15.40", 8888))
    server.listen()
    print("等待客户端连接。。。。。")
    accept1 = threading.Thread(target=acceptThead)
    accept1.start()
    clientA = []
    # send1 = threading.Thread(target=sendinfo)
    # send1.start()
