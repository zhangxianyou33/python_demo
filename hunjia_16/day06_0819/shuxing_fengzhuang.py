class Member():
    def __init__(self,name, age):
        self.__name = name
        self.__age = age
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def inner_change(self, temp):
        self.name = "夏利老师"




if __name__ == "__main__":
    m = Member("tom", 22)
    # print(m.__name)
    # print(m.__age)
    m.set_name("南毛毛")
    m.set_age(999)
    print(m.get_name())
    print(m.get_age())
    m.inner_change(m)  # 传递本类引用
    print(m.get_name())
    print(m.get_age())
