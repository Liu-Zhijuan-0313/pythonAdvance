"""
curentclass 当前类名
parentclassname 当前父类名
attridict 属性按照字典dict存储
"""


def fun(curentclass, parentclassname, attridict):
    print(curentclass, parentclassname, attridict)
    # 类名转小写
    curentclass.lower()
    dict = {}
    for k, v in attridict.items():
        # 排除属性以__和temp开头
        if not k.startswith("__") and not k.startswith("temp"):
            key = curentclass.lower() + k.lower()
            print(key, v)
            # 向字典dict里添加属性
            dict[key] = v
            print(dict)
    return type(curentclass, (), dict)


class Stu(metaclass=fun):
    Name = "lzj"
    genDer = "nv"
    tempA = "aa"


print(hasattr(Stu,"stuname"))