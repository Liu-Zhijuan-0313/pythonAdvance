"""
TCP服务器
"""
import socket
# 1.创建服务器通信对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.配置IP端口
server.bind(("192.168.15.40", 6666))
# 3.开始监听
server.listen()
print("服务器启动")
# 4.获取客户端socket
client, addr = server.accept()
print(client)
print(addr)

while True:
    # 5.接受客户端发送的数据
    data = client.recv(1024)
    print(data.decode("utf-8"))
    # 6.向客户端发送数据
    data1 = input("请输入服务器发送的内容：")
    client.send(data1.encode("utf-8"))
