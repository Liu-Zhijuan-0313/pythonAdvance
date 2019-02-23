"""
 '=': 完全拷贝引用，没有创建内存
 '浅拷贝'：外层创建内存，内层拷贝应用
 '深拷贝': 外层，内层都创建内存

id() 打印对象的内存地址
"""
# l = [1, 2, [3, 4]]
# # l2 = [1, 2, [3, 4]]
# l2 = l
# l2.append(5)
# print(id(l))
# print(id(l2))
# print(l)
# print(l2)
#
# l2[2].append(3.5)
# print(id(l[2]))
# print(id(l2[2]))
#
# print(l)
# print(l2)
"""
= 简单的拷贝引用（拷贝内存地址）,列表外层拷贝引用，内层拷贝引用
"""


# import copy
# l = [1, 2, [3, 4]]
# l2 = copy.copy(l)
# # print(id(l))
# # print(id(l2))
# l.append(5)
# # print(l)
# # print(l2)
#
# print(id(l[2]))
# print(id(l2[2]))
# l2[2].append(3.5)
# print(l)
# print(l2)

"""
浅拷贝：列表外层生成独立内存空间,内层简单拷贝引用（拷贝内存地址）
"""

import copy
l = [1, 2, [3, 4]]
l2 = copy.deepcopy(l)
print(id(l),id(l2))
print(id(l[2]),id(l2[2]))
l.append(5)
l2[2].append(3.5)
print(l)
print(l2)

"""
深拷贝：外层列表拷贝值并且生成独立内存，内层列表拷贝值生成独立内存


"""

