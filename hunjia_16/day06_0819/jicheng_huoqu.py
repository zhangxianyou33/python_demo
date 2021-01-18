# 获取继承的信息，获取父类

class Parant():
    pass

class Message():
    pass

class Sub1(Parant, Message):
    pass

class Sub2(Parant, Message):
    pass


if __name__ == '__main__':
    s1 = Sub1()
    s2 = Sub2()
    m = Message()
    print("下面开始获取实例的父类信息========")
    print("sub1类所属类型：", s1.__class__)
    print("sub2类所属类型：", s2.__class__)
    print("sub2类所属类型：", Sub2.__class__) # 只能判断实例的，不能判断类的
    print("message类所属类型：", m.__class__)

    if s1.__class__ == Sub1:
        print("s1的父类是Sub1！！！")

    print("下面开始获取Parent父类的子类信息========")
    for i in Parant.__subclasses__():   # 只能直接用于主类，不能用于实例对象
        print("子类有：", i)
    print("下面开始获取某个子类是否是指定父类的子类信息========")
    print(issubclass(Sub2, Message))        #判断子类是否源于父类
    print(issubclass(s2.__class__, Parant)) #判断实例化对象，所属的类，是否源于父类
