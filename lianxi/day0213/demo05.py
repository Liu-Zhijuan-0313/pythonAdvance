# yield只能写在函数中
# yield写在函数后，函数中内容的类型变为generator生成器


def fun():
    yield 10
    yield 20
    return "hello world"


result = fun()
print(result)
print(type(result))
print(next(result))
print(next(result))
try:
    print(next(result))
except StopIteration as e:
    print(e)

# 打印裴波拉契算法（从第三项开始均为前两项的和）


def fig(n):
    a, b = 0, 1
    yield a
    yield b
    count = 0
    while True:
        if count < n:
            a, b = b, a+b
            yield b
            count += 1
        else:
            break
    return "finish"


result1 = fig(30)
while True:
    try:
        print(next(result1))
    except StopIteration as e:
        print("next出现异常，原因", e)
        break
