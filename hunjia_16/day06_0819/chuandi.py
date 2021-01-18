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

class P:
    pass

if __name__ == '__main__':
    m1 = Member()
    m2 = Member()
    m1.set_info("tom",22)
    m2.set_info("南毛毛",33)
    print(m2.name)
    print("引用传递地址：",id(m1),id(m2))
    m2 =m1
    print("引用传递地址：",id(m1),id(m2))
    print(m2.name)
    print("======pass类======")
    p = P()
    p.name = "小李老师"
    p.age = 33
    print(id(p.name))
    print(p.name,p.age)


