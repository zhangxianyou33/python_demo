class Member:
    def __init__(self,**kargs):
        self.__name = kargs.get("name")
        self.__age = kargs.get("age")
        self.__children = []
    def get_children(self):
        return self.__children
    def set_car(self,car):
        self.__car = car
    def get_car(self):
        return self.__car
    def get_info(self):
        return "Member类的 年龄：{}，姓名：{}".format(self.__age,self.__name)

class Car:
    def __init__(self,**kargs):
        self.__brand = kargs.get("brand")
        self.__price = kargs.get("price")

