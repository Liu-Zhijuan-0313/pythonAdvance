""""
UDP没有严格的客户端和服务端，UDP客户端不用连接，只管发送不考虑是否发送成功
TCP需要连接服务器
C/S需要客户端，
B/S不需要客户端
"""
import socket
print(socket)
# 创建TCP服务器
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定IP 端口
server.bind(("127.0.0.1", 8989))
# 启动监听
server.listen()
# accept 阻塞方法直到 有客户端连接 cli1代表返回的链接客户端
cli1, addr1 = server.accept()
cli1.send("helloclient")


# 创建UDP客户端
client1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# UDP发送
cli1.sendto()
# UDP接受
client1.recvfrom()


# 创建TCP客户端
client2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接到TCP服务端
client2.connect(("127.0.0.1", 8989))
client2.recv()

