
#继承与 MRO的规则,左边优先
class Base:
    def __init__(self):
        print("this is base")

class Parent_a(Base):
    def __init__(self):
        print("这是子类A===")
class Parent_b(Base):
    def __init__(self):
        print("这是子类B===")

class Sub(Parent_a, Parent_b):
    pass

if __name__ == '__main__':
    s = Sub()
    for i,j  in enumerate(Sub.mro()):
        print("mro顺序为：",j)