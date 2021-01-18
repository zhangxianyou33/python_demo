# 序列结构的for循环，自定义类的迭代，可以通过next实现

class Message:
    def __init__(self, max):
        self.__max = max
        self.__foot = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__foot >= self.__max:
            raise StopIteration()  #如果死循环，停止迭代
        else:
            val = self.__max - self.__foot
            self.__foot += 1
            return val
if __name__ == '__main__':
    m = Message(10)
    for i in m:
        if i ==1:
            break   # 不用break结束，就会死循环
        print(i, end=",")