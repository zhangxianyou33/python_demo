# 子类获取父类的实例化

class Parent:
    def __init__(self):
        print("parent的初始化init")
    def __init_subclass__(cls, **kwargs):
        print("父类parent_subclass:", cls)
        print("父类parent_subclass:", kwargs)

class Sub(Parent, url="www.baidu.com", title="百度"):
    def __init__(self):
        print("子类sub的init")

if __name__ == '__main__':
    sub = Sub()