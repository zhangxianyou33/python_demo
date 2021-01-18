# 合成设计模式，标准化的定义
# 指的是有不同的整体拆分在整合的合成设计模式


class Blackbord:
    pass

class Map:
    pass

class Platform:
    pass

class Desk:
    pass


class Classroom:
    def __init__(self):
        self.__platform = Platform
        self.__blackbord = Blackbord
        self.__map  = Map
        self.__desk = Desk

if __name__ == '__main__':
    pass