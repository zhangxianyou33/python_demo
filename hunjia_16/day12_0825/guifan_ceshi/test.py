#lambda实现简单闭包
#lambda实现闭包
def add(n1):
    return lambda n2: n1 + n2
hello = add(100)
print(hello(200))

