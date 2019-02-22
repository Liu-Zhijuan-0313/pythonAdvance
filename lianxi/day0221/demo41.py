"""
TCP-多人聊天服务器
"""
import socket
from threading import Thread


# 服务器转发消息
def recvinfo(client, formname):
    while True:
        databytes = client.recv(1024)

        # 如果客户端自己关闭断开连接，会一直发给服务器空字符串，
        # 所以需要判断客户端发来的数据是否为空字符串，
        # 如果是空字符，则从服务器关闭客户端，并且从客户端列表移除此客户端
        if len(databytes) == 0:
            client.close()
            clientlist.remove((formname, client))
            break
        else:

            # 对客户端发送的（接受消息的用户|内容）分割
            datastr = databytes.decode("gbk")
            toname = datastr.split("|")[0]
            info = datastr.split("|")[1]
            print(formname, "发给", toname, "消息：", info)

            # 在客户端列表里找到此用户，把内容转发给他，
            # 并说明谁发给他的内容即拼接（发送消息的用户|内容）
            for i in clientlist:
                if i[0] == toname:
                    datastr2 = formname + "|" + info
                    databytes2 = datastr2.encode("gbk")
                    i[1].send(databytes2)


# 等待客户端的连接
def listenaccept():
    while True:
        clientSocket, clientIP = serverSocket.accept()
        # print(clientSocket, clientIP)

        # 接受的第一条信息作为用户名
        # 用户连接到服务器,并添加到客户端列表
        usernamebytes = clientSocket.recv(1024)
        username = usernamebytes.decode("gbk")
        print("用户：", username, "连接上服务器了")
        clientlist.append((username, clientSocket))
        print("当前服务器连接的客户端数量：", len(clientlist))

        # 创建线程接受来自客户端的消息
        recvt = Thread(target=recvinfo, args=(clientSocket, username))
        recvt.start()


#  服务器给所有的客户端发送公告
def sendinfo():
    datastr = input("请输入消息公告：")
    databytes = datastr.encode("gbk")
    for i in clientlist:
        i[1].send(databytes)


if __name__ == '__main__':

    # 1.创建服务器对象
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定服务器地址
    IP = ("192.168.15.40", 6666)
    serverSocket.bind(IP)
    # 3.监听客户端的连接
    serverSocket.listen()
    # 4.创建线程等待客户端的连接，阻塞
    accept1 = Thread(target=listenaccept)
    accept1.start()
    # 5.创建存放客户端的列表
    clientlist = []
    # 6.服务器给所有的客户端发送公告
    sendinfo1 = Thread(target=sendinfo)
    sendinfo1.start()
