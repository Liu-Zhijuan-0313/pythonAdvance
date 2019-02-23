"""
UDP Client
"""
import socket
# 1 创建UDP客户端
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    # 2 发送数据到指定对象
    SERVERADDRESS = ("192.168.15.3", 9001)
    inputstr = input("请输入发送内容")
    client.sendto(inputstr.encode("utf-8"), SERVERADDRESS)
    # 3 客户端调用阻塞方法接受数据
    BUFFERSIZE = 1024
    recvdata, recvaddr = client.recvfrom(BUFFERSIZE)
    print("收到了", recvaddr, "消息", recvdata.decode("utf-8"))
print("客户端结束")
