"""
TCP客户端
"""
import socket
# 1.创建客户端socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.连接到服务器
client.connect(("192.168.15.40", 6666))

while True:
    # 3.向服务端发送数据
    data1 = input("请输入客服端发送的内容：")
    client.send(data1.encode("utf-8"))
    # 4.接受服务端发送的数据
    data = client.recv(1024)
    print(data.decode("utf-8"))

