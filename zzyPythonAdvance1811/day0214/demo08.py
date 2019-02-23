"""
开闭原则：面向修改关闭，面向扩展开放
装饰器（满足开闭原则的设计）
由@符号+语法糖构成
比@classmethod
"""

"封装用户检查方法 有Boss来实现"
def checkuser(fun):
    def check():
        username = input("请输入用户名")
        if username == "wzk":
            print("有权限执行方法")
            fun()
            # showlist()
            # showmoney()
            # showdiscount()
        else:
            print("未授权")
    return check


"查看订单 由程序员A完成"
@checkuser
def showlist():
    print("你的订单有：")
    for i in range(10):
        print("订单" + str(i))

"查看余额 有程序员C完成"
@checkuser
def showmoney():
    "需要操作数据库等复杂操作"
    print("你当前有余额10000￥")

"查看优惠券 有程序员D完成"
@checkuser
def showdiscount():
    print("你有优惠券100 200 300 500")






"展示数据 由程序员B完成"
showlist()
showmoney()
showdiscount()


"""
执行逻辑：
1 调用showlist
2 检测到showlist 有装饰器@checkuser 
没有直接执行showlist 反而将showlist 方法作为参数传递个checkuser
并且执行checkuser 的返回值 即check 方法
"""


