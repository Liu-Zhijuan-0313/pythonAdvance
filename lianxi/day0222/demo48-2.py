"""
1、 F12提取网页html源文件中的网页标题，图片src地址，href链接地址存储为文件
2 、能不能通过python语言提供的库来获取网页源码？requests
"""
import re
import requests


# 第二种方法提供的库来获取网页源码
def getinfo2():
    response = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html")
    content = response.text
    # print(content)
    result = re.findall('<td class="align_center "><a href="//stock.quote.stockstar.com/\d{6}.shtml">(\d{6})</a></td>'
                        '<td class="align_center"><a href="//stock.quote.stockstar.com/\d{6}.shtml">(.*?)</a>', content)
    # print(result)
    return result


def writeinfo2():
    with open("result.txt", "w", encoding="utf-8") as f:
        for i in getinfo2():
            print(i)
            f.write(i[0]+"\t"+i[1])
            f.write("\n")


# 第一种方法下载获取网页源码
def getinfo():
    with open("result.html", "r", encoding="utf-8") as f:
        restr = f.read()
        # print(restr)
        # print(type(restr))
        pattern = '<td class="align_center "><a href="//stock.quote.stockstar.com/\d.*.shtml">(\d.*)</a></td>'
        pattern2 = '<td class="align_center"><a href="//stock.quote.stockstar.com/\d.*.shtml">(\w.*)</a></td>'
        result = re.findall(pattern, restr)
        result2 = re.findall(pattern2, restr)
        # print(result)
        # print(result2)
        return result, result2


def writeinfo():
        with open("result.txt", "w", encoding="utf-8") as f:
            for x in getinfo()[0]:
                for y in getinfo()[1]:
                    f.write(x+"\t"+y)
                    f.write("\n")


if __name__ == '__main__':
    # print(getinfo())
    # writeinfo()
    print(getinfo2())
    writeinfo2()
