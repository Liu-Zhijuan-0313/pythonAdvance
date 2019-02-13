class AI(object):
    # 如果随意添加岂不是封装不安全了？
    # 可以通过__slots__限制添加的内容
    __slots__ = ("name", "hp", "mp")

    def __init__(self, _hp):
        self.hp = _hp


a1 = AI(50)
print(a1.hp)
# 动态的添加类属性 #实例也拥有了该属性
AI.name = "python1811"
print(a1.name)
print(AI.name)
# 动态的添加实例属性
a1.mp = 30
print(a1.mp)
