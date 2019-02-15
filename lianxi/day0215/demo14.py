"""
'=': 完全拷贝引用，没有创建内存
'浅拷贝'：外层创建内存，内层拷贝应用
'深拷贝': 外层，内层都创建内存
id() 打印对象的内存地址
"""
# r1 = [1, 2, [3, 4]]
# r2 = [1, 2, [3, 4]]
# print(id(r1))
# print(id(r2))
# print(id(r1[2]))
# print(id(r2[2]))

# = 简单的拷贝引用，外层和内层地址都相同（都拷贝引用）
# r1 = [1, 2, [3, 4]]
# r2 = r1
# r2.append(10)
# print(r1)
# print(r2)
# print(id(r1))
# print(id(r2))
# print(id(r1[2]))
# print(id(r2[2]))

# 浅拷贝：列表外层生成独立内存空间,内层简单拷贝引用（拷贝内存地址）
# 浅拷贝 外层地址不同，内层地址相同（拷贝引用）
# import copy
# r1 = [1, 2, [3, 4]]
# r2 = copy.copy(r1)
# r2.append(10)
# print(id(r1))
# print(id(r2))
# print(r1)
# print(r2)
# r2[2].append(5)
# print(id(r1[2]))
# print(id(r2[2]))
# print(r1)
# print(r2)

# 深拷贝：外层列表拷贝值并且生成独立内存，内层列表拷贝值生成独立内存
# 深拷贝 外层和内层地址都不同
import copy
r1 = [1, 2, [3, 4]]
r2 = copy.deepcopy(r1)
r2.append(5)
print(id(r1))
print(id(r2))
r1[2].append(10)
print(id(r1[2]))
print(id(r2[2]))
print(r1)
print(r2)