"""
TCP服务端
多线程版本
"""
import socket
from threading import Thread

def recvThread(cli,addr):
    while True:
        databytes = cli.recv(1024*1024)
        # print("收到数据",databytes,"长度为",len(databytes))
        if len(databytes) ==0 :
            # 需要移除断开的客户端
            clilist.remove((addr[1],cli))
            print("客户端",addr,"当前剩余客户端",len(clilist))
            break
        else:
            datastr = databytes.decode("utf-8")
            print(datastr)

def sendThread():
    while True:
        port = input("请指定要接受数据的客户端端口")
        infostr = input("请输入发送的数据")
        infobytes= infostr.encode("utf-8")
        for c in clilist:
            if(c[0] == int(port)):
                c[1].send(infobytes)

def acceptThread():
    while True:
       client, clientaddr = server.accept()
       clilist.append(( clientaddr[1],client ))
       trecv = Thread(target=recvThread, args=(client,clientaddr))
       trecv.start()

if __name__ == "__main__":
    # 1创建服务端套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2绑定IP，端口
    SERVERADDR = ("192.168.15.3", 9999)
    server.bind(SERVERADDR)
    # 3开启监听
    server.listen()
    # 5 服务器需要维护客户端列表 (用户名,socket)
    clilist = []
    # 4开启接受客户端连接的线程
    taccept = Thread(target=acceptThread)
    taccept.start()
    tsend = Thread(target=sendThread)
    tsend.start()