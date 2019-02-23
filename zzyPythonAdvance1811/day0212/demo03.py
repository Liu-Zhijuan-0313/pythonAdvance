"""
动态语言（解释性语言）：执行需要解释器，根据需要去解释代码，边解释边执行，效率低下
Python，JS，PHP，Go，R

编译性语言：需要预先编译成机器语言或者中间语言，效率高
C++，C
C#，Java

很多Python库库使用C语言来编写 import math
胶水语言（自己不实现，通过调用其他语言的实现）

Python如何动态的
"""

"""
通过类名添加类属性
通过实例名添加实例属性
实例权限比较高
"""

class Person(object):
    "表名只有name 和mp,hp属性可以被动态的添加"
    __slots__ = ("name", "mp", "hp")
    "类属性"
    isAlive = False
    def __init__(self,_hp):
        self.hp = _hp

"声明p的时候还没有类属性"
p = Person(100)
p1 = Person(100)
"通过类名动态的添加类属性"
Person.name = "zzy"
"实例可以获取类属性"
print(p.name,Person.name)
"通过实例动态的添加实例属性"
p.mp = 50
print(p.mp)
print(p1.name)


#wheelnum 没有通过 __slots__的审核所以不能被动态添加
p.wheelnum = 4
print(p.wheelnum)

