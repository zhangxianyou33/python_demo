class A:
    def hello(self):
        print("hello,这是第一个对象。")
a = A()
a.hello()

class Member():
    """
    类中属性定义
    """
    def set_info(self, name, age):
        """
        :return:
        """
        self.name = name
        self.age = age
    def get_info(self):
        return "姓名：{},年龄：{}".format(self.name, self.age)

if __name__ == '__main__':
    m = Member()
    m.set_info("tom",22)
    print(m.get_info())
    print(type(m.get_info))
    print(m.name)
    # 实例属性。类属性。实例属性可以在外面扩充访问
    m.score = "张显友"
    print(m.score)




