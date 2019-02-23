"""
*******以下代码紧在linux执行  fork不支持windows
"""
import os
print(os.getpid())
print("begin")
returncode = os.fork() #create process   2
# print()
print(returncode ,"current process ", os.getpid(), "parent process", os.getppid())
# fork()  create process
# main process fork return  child process id
# child process fork return 0
# getpid() get current process id
# getppid() get parent process id
