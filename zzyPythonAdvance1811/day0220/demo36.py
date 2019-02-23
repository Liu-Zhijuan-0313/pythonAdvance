"""
TCP 服务端
"""
import socket
# 创建服务端通信对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# p配置IP端口
SERRVERADDR = ("192.168.15.3", 6666)
server.bind(SERRVERADDR)
# 开启监听
server.listen()
print("服务端启动")
# 获取客户端socket
client,clientaddr = server.accept()
print("客户端",clientaddr,"连接上了")
# 接受客户端发送的数据
BUFFERSIZE = 1024
data = client.recv(BUFFERSIZE)
print(data.decode("utf-8"))
client.send("你好客户端".encode("utf8"))

