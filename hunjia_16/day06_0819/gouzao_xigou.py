# 构造方法 __init__
# 是起点，不许有返回值
# 一个类只有一个构造方法
# 如果没有构造方法，需要通过实例化对象。set方法

#定义一个五参数的构造方法,进行类的初始化

class Member:
    def __init__(self):
        print("这是构造方法")

class P:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return self.name,self.age


# 构造方法中使用关键字参数
class  A:
    def __init__(self, **kwargs):
        self.__name = kwargs.get("name")
        self.__age = kwargs.get("age")
    def get_info(self):
        return self.__name, self.__age


# 析构函数
class B:
    def __init__(self, **kwargs):
        print("当前是析构方法",id(self))
        self.__name = kwargs.get("name")
        self.__age = kwargs.get("age")
    def __del__(self):
        print("资源马上回收：", id(self))
    def get_info(self):
        return self.__name, self.__age
if __name__ == '__main__':
    m = Member()
    b = Member()
    print(dir(m))
    for i in dir(m):
        if i == "__init__":
            print("找到了")
    p = P("张显友", 77)
    print(p.name, p.age)
    print("============")
    a = A(name="jack", age = 88)
    print(a.get_info())
    aa = A(name="张三")
    aaa = A(age=100)
    print(aa.get_info())
    print(aaa.get_info())
    print("析构函数,进行收尾处理")
    b = B()
    bb = B(name= "bb", age=111)
    print(id(b), id(bb))
    print(b.get_info())
    print(bb.get_info())
    del bb  # 删除对象，调用析构方法
    print(b.get_info())