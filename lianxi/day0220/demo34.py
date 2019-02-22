"""
UDP Server
"""
import socket

# 1.创建UDP服务器
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2.服务器的绑定IP+端口
# 端口不建议使用0到1023
server.bind(("192.168.15.40", 6666))

while True:
    # 3.recvaddr从哪个客户端收到的,即对方的IP+端口
    #   recvdata 对方发送的信息内容
    #   recvfrom中的bufsize: 1024表示1k
    recvdata, recvaddr = server.recvfrom(1024)
    print("收到了", recvaddr, "信息:", recvdata.decode("utf-8"))

    # 4.发送数据到指定对象
    data = input("请输入发送的内容：")
    server.sendto(data.encode("utf-8"), recvaddr)

# 5.关闭服务器
server.close()
print("finish")

# input和recvfrom和accept都可以阻塞
