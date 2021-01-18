#对象是引用数据类sing，描述内存地址
"""
常用判断：eq   lq   bq

"""
class Member:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __lt__(self, other): # 需要传入比较对象
        if not isinstance(other, Member) or other == None:
            return False
        else:
            return self.__age <= other.__age  # 小于等于为True

class Me:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __eq__(self, other):
        if not isinstance(other, Me) or other == None:
            return False
    def __str__(self):
        return "姓名：{}，年龄：{}".format(self.__name,self.__age)
    def __bool__(self):
        return self.__age > 18
if __name__ == '__main__':
    m = Member("张三", 22)
    b = Member("tom", 33)
    print("比较结果为：",m.__lt__(b))
    print("====序列操作演示======")
    m_list = [Me("peter",30), Me("pack",30)]
    for i in m_list:
        print(i)
# 有了特殊方法，更方便开发
    print("bool方法校验：======")
    m1 = Me("李四",30)
    if m1:
        print("已经成年了")
