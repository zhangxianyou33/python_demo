# 所有的类都是父类，是新式类
# python2版本,类分为两种，
# 古典类：classictype ，不继承object，在解决MRO问题采用深度优先
# 新式类：class type， 继承object，在解决MRO问题，广度优先

#object类，只是定义了一些基本的公共操作行为，但是内部的大多数方法
class Message(object):
    pass

class Me:
    pass

if __name__ == '__main__':
    print(type(Me))
    print(type(Message))