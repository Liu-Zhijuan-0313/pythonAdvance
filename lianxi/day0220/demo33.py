import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1000))
""""
UDP没有严格的客户端和服务端，不用连接，只管发送不考虑是否发送成功
C/S需要客户端，
B/S不需要客户端
"""