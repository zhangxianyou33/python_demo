# __new__()构造器，在对象实例化中，
# init并不是最早调用,是在new后面的
# 大部分new的实例化对象不会使用，都是用init
# 利用其方法产生构造信息


class Message:
    def __new__(cls, *args, **kwargs):
        print("new:",args, kwargs)
        return object.__new__(cls)
    def __init__(self, **kwargs):
        print("init:", kwargs)


if __name__ == '__main__':
    m = Message(name="tom", age=33)