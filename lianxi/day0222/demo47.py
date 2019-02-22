"""
正则表达式
"""
"""
得到Match对象可以使用group方法：
    1.match从头开始匹配
    2.search从出现的位置开始匹配，只匹配第一个
    3.fullmatch从头匹配到尾，内容完全相同才可以匹配到
    4.finditer返回迭代器，迭代器中每一个元素都是Match对象都有group方法
得到列表：
    5.findall可以匹配所有内容,全文搜索匹配，每次出现都放入列表中
    6.split使用正则切割字符串
得到字符串：
    7.sub用新字符串替换能够被正则匹配的内容


complite 可以得到一个pattern模型，进而通过模型调用响应方法
         Python通过re模块提供对正则表达式的支持。
         使用re的一般步骤是先使用re.compile()函数，
         将正则表达式的字符串形式编译为Pattern实例，
         然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），
         最后使用Match实例获得信息，进行其他的操作。


第三个参数flags作为可选参数：
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
    
    
表示数量：
    *      可以匹配前一个字符出现 >=0
    +      可以匹配前一个字符出现 >=1
    ？     可以匹配前一个字符出现 0或1
    {m}    可以匹配前一个字符出现 m次
    {m,}   可以匹配前一个字符出现 >=m次
    {m,n}  可以匹配前一个字符出现 m到n次,出现n次则匹配n,次数从多到少
    
表示边界：
    ^  以什么开头
    $  以什么结尾
    \b 单词边界
    \B 非单词边界
    1.从这些分割的字符串中我们可以知道单词边界就是单词和符号之间的边界
    这里的单词可以是中文字符,英文字符,数字；符号可以是中文符号,英文符号,空格,制表符,换行
    空格并不是边界 空格与数字2之间的那个才叫边界
    2.\b是单词与符号的边界 那非单词与符号的边界的其它都是\B
    所以我们的猜想\B是符号与符号,单词与单词的边界
    
匹配分组：
    \ 匹配左右任意一个表达式 
    (ab) 将括号中字符作为一个分组，利用group(数字)可以找到第几组匹配的内容
    \num 引用分组num匹配到的字符串，(num表示第num个分组，\num表示第num个分组的内容相同）
    (?P<a>aaa).*(?P=a)  aaa的别名为a，后面如果内容和aaa相同，可以用(?P=a)表示
                        group(数字)也可以用group(P=a)
"""
import re
# print(dir(re))
# pattern = "1811"
# restr = "py1811hel1811lo18111811"

# result = re.match(pattern, restr)
# result = re.search(pattern, restr)
# result = re.fullmatch(pattern, restr)

# result = re.findall(pattern, restr)
# result = re.split(pattern, restr)
# result = re.sub(pattern, "a", restr)

# result = re.finditer(pattern, restr)
# print(result, type(result))
# for i in result:
#     print(i, type(i))

# print(result, type(result))


# result = re.match(r"(?P<hname>hello) world (?P=hname)", "hello world hello china")
# print(result.group("hname"))

