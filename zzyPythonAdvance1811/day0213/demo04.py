"""
给类或者实例动态添加方法
方法:
1,实例方法
"""
import types
class Person(object):
    """Person类可以动态的添加各种方法"""

    def __init__(self, _name):
        self.name = _name

"添加实例方法 getname  setname"
def setname(self, newname):
    self.name = newname

def getname(self):
    return self.name

"添加类方法getdesc"
@classmethod
def getdesc(cls):
    return cls.__doc__

" 动态添加类方法"
Person.getd = getdesc


"添加静态方法getinfo"
@staticmethod
def getinfo():
    return "helloworld"

"动态添加静态方法"
Person.geti = getinfo



p1 = Person("zzy")
p2 = Person("abc")

"需要获取角色的名字"
"1 通过实例名"
"2 添加一个可以设置实例名的方法"
"实例方法的添加需要使用types模块"


p1.setn = types.MethodType(setname, p1)
p1.getn = types.MethodType(getname, p1)
p2.getn = types.MethodType(getname, p2)
p1.setn("zzy1")
# print(p1.getn())
# print(p2.getn())

# print(Person.getd())
# print(p1.getd(),p2.getd())

print(Person.geti())

"动态语言 边执行边解释"


