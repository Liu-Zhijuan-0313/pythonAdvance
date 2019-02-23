import socket
print(socket)
# TCP
# 创建TCP服务器
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定IP 端口
server.bind(("127.0.0.1", 8989))
# 启动监听
server.listen()
# accept 阻塞方法直到 有客户端连接 cli1代表返回的链接客户端
cli1,addr1 = server.accept()
cli1.send("helloclient")
# UDP发送
cli1.sendto()
# 创建TCP客户端
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接到TCP服务端
client.connect(("127.0.0.1", 8989))
client.recv()
# UDP接受
client.recvfrom()