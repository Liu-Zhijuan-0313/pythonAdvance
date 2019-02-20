"""
UDP client
"""
import socket

# 1.创建UDP客户端
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:

    # 2.发送数据到指定对象
    serveraddress = ("192.168.15.40", 666)
    data = input("请输入发送内容：")
    client.sendto(data.encode("utf-8"), serveraddress)

    # 3.recvaddr从哪个客户端收到的,即对方的IP+端口
    #   recvdata 对方发送的信息内容
    recvdata, recvaddr = client.recvfrom(1024)
    print("收到了", recvaddr, "信息", recvdata.decode("utf8"))

# 关闭客户端
client.close()
print("finish")
