"""
TCP客户端
"""
import socket
# 创建客户端socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接到服务端
SERVERADDR = ("192.168.15.3", 6666)
client.connect(SERVERADDR)
# 向服务端发送数据
client.send("你好服务器".encode("utf-8"))
BUFFERSIZE = 1024
data= client.recv(BUFFERSIZE)
print("收到服务发来",data.decode("utf-8"))