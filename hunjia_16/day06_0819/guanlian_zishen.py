# 关联后的子类问题
class People:
    def __init__(self, **kwargs):

        self.name = kwargs.get("name")
        self.age = kwargs.get("age")
        self.children = [] # 表示全部子类，或者后代
    def get_children(self):
        return self.children
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
    p = People(name="南毛毛",age=28)
    c = Car(brand="宝马",price=110000)
    print(p.get_info())
    print(c.get_info())

    print("开始互相关联=============") # 利用引用的机制，进行关联设计

    p.set_car(c)
    c.set_people(p)
    print(p.get_car().get_info())   # 通过车获取人的信息
    print(c.get_people().get_info()) # 通过人获取车的信息

    print("自身关联属性演示=========")
    ch_a = People(name="团团",age=777)
    ch_b = People(name="滚滚", age=777)
    car_a = Car("大众",9999)
    car_b = Car("丰田",9999)
    ch_a.set_car(car_a)
    ch_b.set_car((car_b))
    car_a.set_people(ch_a)
    car_b.set_people(ch_b)
# 开始设置父子关系
    p.get_children().append(ch_a)
    p.get_children().append(ch_b)
    print("开始输出信息-------------")
    print("父辈信息:",p.get_info())
    print("父辈车的信息：",p.get_car().get_info())
    for i in p.get_children():
        print("\t子类信息：", i.get_info())
        print("\t",i.get_car().get_info())
