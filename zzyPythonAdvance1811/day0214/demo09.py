"""
装饰器的形成
"""

def checkuser(fun):
    def check():
        username = input("请输入用户名")
        if username == "wzk":
            print("有权限")
            fun()
        else:
            print("未授权")
    return check
def shoulist():
    print("展示列表成功")


# result = checkuser(shoulist)
# result()
shoulist = checkuser(shoulist)

shoulist()