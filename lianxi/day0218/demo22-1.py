"""
进程池带参数，
子进程修改参数之后，主进程不改变
主进程修改参数之后，子进程不改变
"""
from multiprocessing import Pool
import time


def processmain(num, listA, listB):
    # print("bejin", num)
    num = 200
    listA.append(4)
    listB.append(100)
    print("子进程执行完毕，num值为", num)
    print("子进程执行完毕，list值为", listA)
    print("子进程执行完毕，list值为", listB)


def main():
    num = 100
    listA = [1, 2, 3]
    listB = [1, 2, 3, [4, 5]]
    pool = Pool(5)
    pool.apply_async(func=processmain, args=(num, listA, listB))
    pool.close()
    pool.join()
    num = 4
    print("主进程执行完毕，num值为", num)
    print("主进程执行完毕，list值为", listA)
    print("主进程执行完毕，list值为", listB)


if __name__ == '__main__':
    main()
