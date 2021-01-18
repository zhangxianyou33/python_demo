# 继承与构造方法


#继承构造方法很特殊，子类没有定义可以直接用父类的
class Parent:
    def __init__(self):
        print("这是父类的构造方法!")
class Sub(Parent):
    pass

class S2(Parent):
    def __init__(self):
        print("这是子类的构造====方法")
class Sub3(Parent):
    def __init__(self):
        print("这是子类的，方法*******")
    def fun(self):
        super().__init__()    #子类使用父类的构造方法


# 当子类有构造方法，优先使用子类的构造方法，也可以手动调用父类的构造方法



if __name__ == '__main__':
    s = Sub()
    s2 = S2()
    print("======下面是子类使用父类的构造方法=====")
    s3 = Sub3()
    s3.fun()
# 在进行继承关系的时候，子类可以继续通过父类构造进行某些，父类对象实例化的初始化操作