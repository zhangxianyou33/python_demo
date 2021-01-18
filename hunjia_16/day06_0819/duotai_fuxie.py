#在类的继承中，子类使用父类方法，进一步扩充完整，使用覆写功能

class A:
    def hello(self):
        print("父类的方法：hello word")


class B(A):
    def hello(self):     # 覆写父类的方法
        super().hello()  # 调用父类的方法
        print("子类覆写方法：你好啊！")


if __name__ == '__main__':
    b = B()
    b.hello()