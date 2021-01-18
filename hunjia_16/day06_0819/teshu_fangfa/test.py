class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(self.name)
        print(self.age)


obj1 = Foo('wupeiqi', 18)
obj1.get_info()
"""
默认会将obj1传给self参数,即：obj1.detail(obj2)，
此时方法内部的 self ＝ obj1，即：self.name 是 wupeiqi ；self.age 是 18
"""
