# 1."实现基础闭包语法"
def user():
    print("username")

    def student():
        print("lzj")
    return student


result = user()
result()
