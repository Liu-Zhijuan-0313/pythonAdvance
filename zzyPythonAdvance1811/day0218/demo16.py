"""
元类用来创建类
type（类名字符串，父类列表，类中属性）
元类的用法：
私有属性：_name
不可访问实行：__name__
"""

# def move(self, _speed):
#     print("ai速度为", str(_speed))
#
# AI = type("AI", (object,), {"name": "ai1", "move": move})
# # print(dir(AI))
# # print(AI.__dict__)
#
# NPC = type("NPC", (AI,), {})
# print(NPC.__bases__)

# Python 是动态语言， 动态添加属性

"""
Python 在内存中创建类之前需要现在类中查找metaclass属性 
如果没有就去父类，父类也没有就去模块中查找
找到metaclass之后则使用metaclass类中方法创建
否则就需要使用type创建
"""


"""
要求：所有的属性均要以小写类名+小写属性
"""
"""
metaclass 存储的方法才是真正类的创建过程
"""
def mydesignclass(curentclass, parentclassname, attrdict):
    "使用这个方法去创建真正的NPC类"
    # print(curentclass, parentclassname, attrdict)
    # print(curentclass.lower())
    newclassattrdict = {}
    for k,v in attrdict.items():
        if not k.startswith("__"):
            # print(curentclass.lower()+k.lower(),v)
            newclassattrdict[curentclass.lower()+k.lower()] = v
    print(newclassattrdict)
    "在使用type创建类之前需要对原始类进行修改  比如属性重命名"
    return type(curentclass, (), newclassattrdict)

class NPC(metaclass=mydesignclass):
    "npcspeed  npcname"
    Speed = 10
    name = "ai1"

print(hasattr(NPC, "Speed"))
print(hasattr(NPC, "npcspeed"))


"""
1,使用关键字class创建NPC
2，python解释器需要常见NPC之前 去NPC内部检查有没有metaclass属性
3，检测到有metaclass属性则使用metaclass方法创建类
4，比如需要重命名属性
5，使用type将新类返回
"""


