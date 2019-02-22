"""
HTTP TCP 编写Web服务器
客户端建立连接后，服务器做出响应就断开连接，
客户端每次请求都要进行重新连接，即无while True
"""
"""
传输层：UTP，TCP
应用层编程：HTTP, FTP, SNIP
HTTP:超文本传输协议，底层使用的是TCP协议
无状态协议：打开之后立即关闭

请求结构：
    1.请求行：请求方法 URL 协议版本
            GET /index.html HTTP/1.1
    2.请求头：键：值，每一行为一个键值对
            User-Agent:python
            Accept:*
    3.空行：标识请求头已经结束
    4.请求体：常用语POST时有内容

响应结构：
    1.响应行：协议版本 状态码 状态描述
              HTTP/1.1 200 OK
    2.响应头：键：值，每一行为一个键值对
             Content-Type：text/html
    3.空行：标识响应头结束
    4.响应体
"""
import socket
from threading import Thread


# 客户端为了得到页面数据，向服务器发送请求，服务器做出响应
def recvinfo(cli):
    print(cli.getpeername(), "连接了")
    databytes = cli.recv(1024)

    # 客户端向服务器发送空字符串
    if len(databytes) == 0:
        print(cli.getpeername(), "断开了")
    else:
        datastr = databytes.decode("utf-8")
        # print(datastr)
        # 以空格分割得到路径URL
        filename = datastr.split(" ")[1]
        print(filename)


        # 响应即把数据内容返回到页面
        responseline = "HTTP/1.1 200 OK\r\n"
        responseHeader = "Content-Type：text/html\r\n"
        responseNULLline = "\r\n"
        try:
            with open("templates" + filename, "rb") as f:
                responseBody= f.read()
        except:
            with open("templates/404.html", "rb") as f:
                responseBody = f.read()
        cli.send(responseline.encode("utf-8"))
        cli.send(responseHeader.encode("utf-8"))
        cli.send(responseNULLline.encode("utf-8"))
        cli.send(responseBody)


    cli.close()


# 创建线程等待客户端的连接
def listenaccept():
    while True:
        clientSocket, clientaddr = serverSocket.accept()
        # print(serverSocket)
        # print(clientaddr)

        # 创建线程等待接受客户端的消息
        recvinfo1 = Thread(target=recvinfo, args=(clientSocket, ))
        recvinfo1.start()


if __name__ == '__main__':
    # 1.创建服务器对象
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定服务器地址
    IP = ("192.168.15.40", 9999)
    serverSocket.bind(IP)
    # 3.监听
    serverSocket.listen()
    # 4.创建线程等待客户端的连接
    listenaccept1 = Thread(target=listenaccept)
    listenaccept1.start()
