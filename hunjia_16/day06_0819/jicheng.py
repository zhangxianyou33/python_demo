#对已有的类功能扩充
#全面继承父类，包括类的：构造，属性，方法
#在不需要修改已有类的前提下，对已有类的功能进行扩充

class People:
    def __init__(self):
        self.__name = None
        self.__age = 0
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
class Student(People):   #继承People类的功能
    def __init__(self):
        self.__score = None
        self.__school = None
    def set_score(self, score):
        self.__score = score
    def get_score(self):
        return self.__score
    def set_school(self, school):
        self.__school = school
    def get_school(self):
        return self.__school

if __name__ == '__main__':
    s = Student()
    s.set_name("张三")
    s.set_age(60)
    print(s.get_name())
    print(s.get_age())
    print("子类属性============")
    s.set_school("实验中学")
    print("学生学校是：",s.get_school())

