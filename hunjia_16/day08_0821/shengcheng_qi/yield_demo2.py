# 根据另外一个生成器创建操作序列
def fibonacci(max=99):
    a, b = 0, 1
    while a < max:
        # print(a, end=",")
        yield b
        a, b = b , a+b
def fibo_yield(func):
    yield from func
if __name__ == '__main__':
    # fibonacci()
    res = fibo_yield(fibonacci(66))
    for i in res:
        print(i, end=",")