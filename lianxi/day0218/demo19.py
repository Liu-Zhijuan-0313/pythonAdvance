"""
fork只能在Linux上运行
子进程fork方法的返回0，父进程fork方法的返回子进程的pid
当前进程：os.getpid()
当前进程的父进程：os.getppid()
"""
# 1.在Linux的进程
# import os
# print(os.getpid())
# pid = os.fork()
# if pid == 0:
#     print("子进程id %s, 父进程id %s" % (os.getpid(), os.getppid()))
# else:
#     print("父进程id %s, 子进程id %s" % (os.getpid(), os.getppid()))
