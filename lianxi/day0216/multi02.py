# 无参数的进程池
from multiprocessing import Pool
import os
import time


def fun():
    print("pid %d" % os.getpid())


def main():
    pool = Pool(2)
    for i in range(3):
        # pool.apply(fun)
        pool.apply_async(fun)
        time.sleep(1)
    pool.close()
    pool.join()
    print("finish")


if __name__ == '__main__':
    main()
# 2.非阻塞进程池
# from multiprocessing import Pool
# import os
# import time
#
#
# def fun(name, age, **kwargs11):
#     print("pid %d" % os.getpid())
#     print(name, age, kwargs11)
#
#
# def main():
#     pool = Pool(5)
#     for i in range(10):
#         pool.apply(fun, args=("lzj", 20), kwds={"gender": "nv"})
#         time.sleep(1)
#     print("finish")
#
#
# if __name__ == '__main__':
#     main()

# 3.阻塞进程池
# from multiprocessing import Pool
# import os
# import time
#
#
# def fun(name, age, **kwargs11):
#     print("pid %d" % os.getpid())
#     print(name, age,kwargs11)
#
#
# def main():
#     pool = Pool(5)
#     for i in range(10):
#         pool.apply_async(fun, args=("lzj", 20), kwds={"gender": "nv"})
#         time.sleep(1)
#     pool.close()
#     pool.join()
#     print("finish")
#
#
# if __name__ == '__main__':
#
#     main()
#