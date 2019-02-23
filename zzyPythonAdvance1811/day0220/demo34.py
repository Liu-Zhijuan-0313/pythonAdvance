"""
UDP Server
"""
import socket
# 1创建UDP服务器
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2绑定服务端的IP 端口
SERVERADDRESS = ("192.168.15.3", 9001)
server.bind(SERVERADDRESS)
# 2开始使用阻塞方法接受消息
BUFFERSIZE = 1024

while True:
    recvdata, recvaddr = server.recvfrom(BUFFERSIZE)
    print("收到了", recvaddr, "信息", recvdata.decode("utf-8"))
    server.sendto(recvdata, recvaddr)
print("服务收到了消息并作出了响应")
