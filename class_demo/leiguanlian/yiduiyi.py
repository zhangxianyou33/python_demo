class Member:
    def __init__(self,**kargs):
        self.__name = kargs.get("name")
        self.__age = kargs.get("age")
    def set_car(self,car):
        self.__car = car
    def get_car(self):
        return self.__car
    def get_info(self):
        return "Member类姓名：{}，年龄：{}".format(self.__name,self.__age)
class Car:
    def __init__(self,**kargs):
        self.__brand = kargs.get("brand")
        self.__price = kargs.get("price")
    def set_member(self,member):
        self.__member = member
    def get_member(self):
        return self.__member
    def get_info(self):
        return "Car  类的汽车品牌：{}，价格为：{}".format(self.__brand,self.__price)
if __name__ == '__main__':
    def zhu():
        mem = Member(name="张显友",age=50)
        car = Car(brand="奔驰",price=30000)
        mem.set_car(car)
        car.set_member(mem)
        print(mem.get_car().get_info())
        print(car.get_member().get_info())
    zhu()

