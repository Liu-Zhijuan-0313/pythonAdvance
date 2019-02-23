"""
元类用来创建类
type（类名字符串，父类列表，类中属性）
元类的用法：
_表示为私有属性:_name
查找继承的父类：类名.__bases__
issubclass(a,b)能够測试继承关系，a是否继承了b
"""

"""
__bases__类似于Javascript中Object对象的__proto__，
是实现继承的基础，不同在于：__bases__不可修改，
而且__bases__是类的属性而不是对象属性
（Javascript是基于对象的语言）
"""


# def move(_speed):
#     print("速度为", str(_speed))
#
#
# AI = type("AI", (object, ), {"name": move})
# print(AI.__dict__)
# print(dir(AI))
# a = AI.name
# print(a)
# print(a(10))


# NPC = type("NPC", (AI, ), {})
# print(NPC.__bases__)
# print(NPC.__dict__)
# print(NPC.__name__)
# print(issubclass(NPC, AI))
# Python是动态语言，动态添加属性

"""
python在内存中创建类之前需要先在类中查找metaclass属性
如果没有就去父类，父类也没有就去模块中查找
找到metaclass之后则使用metaclass类中方法创建
否则就需要使用type创建
hasattr(NPC, "npcspeed")判断NPC类中是否有此属性

"""
"""
# 要求：所有的属性要以小写类名+小写属性
# metaclass存储的方法才是真正类的创建过程
curentclass 当前类名
parentclassname 当前父类名
attridict 类中的属性,按照字典dict存储
"""


# 修改之前类的属性，并使用元类创建新类
def mydesignclass(curentclass, parentclassname, attridict):
    print(curentclass, parentclassname, attridict)
    newattridict = {}
    for k, v in attridict.items():
        if not k.startswith("__"):
            print(k, v)
            key = curentclass.lower()+k.lower()
            newattridict[key] = v
            print(newattridict)
    return type(curentclass, (), newattridict)


class NPC(metaclass=mydesignclass):
    Speed = 10
    name = "lzj"


# 判断NPC类中是否有此属性
print(hasattr(NPC, "npcspeed"))
print(hasattr(NPC, "npcname"))



"""

1,使用关键字class创建NPC
2，python解释器需要常见NPC之前 去NPC内部检查有没有metaclass属性
3，检测到有metaclass属性则使用metaclass方法创建类
4，比如需要重命名属性
5，使用type将新类返回
"""