import multiprocessing
import time

class Mypro(multiprocessing.Process):
    def __init__(self, name, delay, count):
        super().__init__(name=name) # 同时使用父类和子类的初始化
        self.__delay = delay
        self.__count = count
    def run(self):
        for i in range(self.__count):
            print("{}=进程id为：{}， 进程名字为：{}".format(i,
                        multiprocessing.current_process().pid,
                        multiprocessing.current_process().name))
            time.sleep(1)  # 减慢代码执行速度
if __name__ == '__main__':
    for i in range(3):
        #创建进程对象
        pro = Mypro(name="类进程-{}".format(i),
                    delay=1,
                    count=10)
        pro.start() #进程启动