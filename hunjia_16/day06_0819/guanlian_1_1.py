class People:
    def __init__(self, name, age):

        self.name = name
        self.age = age
    def get_info(self):
        return self.name, self.age

    def set_car(self, car):
        self.car = car
    def get_car(self):
        return self.car  # 获取人对应车的信息

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def get_info(self):
        return self.brand, self.price

    def set_people(self, people):  #定义车和人的关系
        self.people = people

    def get_people(self):
        return self.people

if __name__ == "__main__":
    p = People("南毛毛",28)
    c = Car("宝马",110000)
    print(p.get_info())
    print(c.get_info())

    print("开始互相关联=============") # 利用引用的机制，进行关联设计

    p.set_car(c)
    c.set_people(p)
    print(p.get_car().get_info())   # 通过车获取人的信息
    print(c.get_people().get_info()) # 通过人获取车的信息