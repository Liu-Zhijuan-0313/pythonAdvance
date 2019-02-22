"""
通过python语言提供的库来获取网页源码
"""
# import requests
# response = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html")
# print(response.text)

# 案例
import re
import requests


# 第二种方法提供的库来获取网页源码
def getinfo2():
    response = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html")
    content = response.text
    result = re.findall(
        '<td class="align_center "><a href="//stock.quote.stockstar.com/\d{6}.shtml">(\d{6})</a></td>'
        '<td class="align_center"><a href="//stock.quote.stockstar.com/\d{6}.shtml">(.*?)</a>',
        content)
    return result


# 第一种方法下载获取网页源码
def getinfo():
    with open("result.html", "r", encoding="utf-8") as f:
        content = f.read()
        # print(content)
    result = re.findall(
        '<td class="align_center "><a href="//stock.quote.stockstar.com/\d{6}.shtml">(\d{6})</a></td>'
        '<td class="align_center"><a href="//stock.quote.stockstar.com/\d{6}.shtml">(.*?)</a>',
        content)
    return result



def writefile():
    # print(getinfo())
    with open("result.txt", "w", encoding="utf-8") as f:
        for r in getinfo2():
            f.write(r[0] + "\t" + r[1])
            f.write("\n")


if __name__ == "__main__":
    writefile()
    # print(getinfo2())
