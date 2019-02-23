"""
工具模块
提供各种方便的操作
"""

class Utils(object):
    "实现一个比较大小的方法"
    @staticmethod
    def max(a,b):
        if a>b:
            return a
        else:
            return b

    @staticmethod
    def power(a,b):
        return a**b
