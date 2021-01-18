# 所有类都是object类，获得对象所在类的名称

# 如果一个类的对象，有自己的直接输出要求，可以覆写此方法，来实现
class Message:
    def __init__(self, connection):
        self.__connection = connection

class Me:
    def __init__(self, content):
        self.__content = content
    def __str__(self):
        return "覆写str方法,被调用了,{}".format(self.__content)
    def __repr__(self):
        return "覆写repr方法，被调用了{}".format(self.__content)

class M:
    def __init__(self, content):
        self.__content = content
    def __str__(self):
        return "覆写str方法,被调用了,{}".format(self.__content)
    def __repr__(self):
        return "覆写repr方法，被调用了{}".format(self.__content)
    __repr__ = __str__
if __name__ == '__main__':
    m = Message("小李老师")
    print(m)    # 获取对象信息
    print(m.__str__())
    print(m.__repr__())

    print("==========覆写方法演示========")
    me = Me("hello word")
    print(me)
    print(me.__str__())
    print(str(me))
    print("==========repr覆写方法演示========")
    print(me.__repr__())
    print(repr(me))
# repr是留给开发者使用的，在交互式的环境中，看出用户的原来输入情况
    print("==========repr开发交互方法演示========")
    res = Me("    hello    ")
    print(repr(res))
    print("==========repr和str演示========")
    m = M("repr he str 相等")
    print(str(m))
    print(repr(m))
