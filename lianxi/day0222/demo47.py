"""
正则表达式
"""
"""
得到Match对象：
    1.match从头开始匹配
    2.search从出现的位置开始匹配，只匹配第一个
    3.fullmatch从头匹配到尾，内容完全相同才可以匹配到
得到列表：
    4.findall可以匹配所有内容,全文搜索匹配，每次出现都放入列表中
    5.split使用正则切割字符串
    6.sub用新字符串替换能够被正则匹配的内容
得到Match对象
7.finditer返回迭代器，迭代器中每一个元素都是Match对象
complite Python通过re模块提供对正则表达式的支持。
         使用re的一般步骤是先使用re.compile()函数，
         将正则表达式的字符串形式编译为Pattern实例，
         然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），
         最后使用Match实例获得信息，进行其他的操作。


flags作为可选参数：
    例如：flags = re.I|re.S|re.M
    |    表示同时使用
    re.I 不区分大小写
    re.S 单行模式，包括换行符，在单行模式下.符号可以匹配\n
    re.M 多行模式，（"^"匹配字符串开始以及"\n"之后；"$"匹配"\n"之前以及字符串末尾）



字符匹配：
    .  匹配任意字符，不包括换行符 (单行模式下包括换行符)
    [] 可以匹配其中一个[0-9a-zA-z]
    \d 匹配所有的数字，即0-9
    \D 匹配非数字
    \s 匹配空格或者制表符Tab键，\t
    \S 匹配非空格和非制表符
    \w 匹配字母a-z,A-z,0-9,_
    \W 匹配非字母
    
"""
import re
# print(dir(re))
pattern = "1811"
restr = "py1811hel1811lo18111811"

# result = re.match(pattern, restr)
result = re.search(pattern, restr)
# result = re.fullmatch(pattern, restr)

# result = re.findall(pattern, restr)
# result = re.split(pattern, restr)
# result = re.sub(pattern, "a", restr)

result = re.finditer(pattern, restr)
print(result, type(result))
for i in result:
    print(i, type(i))

# print(result, result.group(), type(result))

