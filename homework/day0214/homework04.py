import time


def counttime(fun):
    a = time.time()

    def count():
        print("统计时间")
        fun()
        b = time.time()
        print(b - a)

    return count


@counttime
def showlist():
    print("订单列表")
    time.sleep(1)


showlist()


@counttime
def showmoney():
    print("用户余额")
    time.sleep(1)


showmoney()