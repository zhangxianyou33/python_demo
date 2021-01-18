# 类方法，是为了弥补，init构造方法的缺陷问题
# 假如init构造方法，定义了俩参数，但是临时需要接收一个复核参数，
class Message:
    @classmethod
    def get_info(info):
        info().hello() #本类对象，调用本类方法
    def hello(self):  #类中的普通方法
        print("这是方法：hello")

class Me:
    def __init__(self, title, url):
        self.__title = title
        self.__url = url
    def __str__(self):
        return  "{},{}".format(self.__title, self.__url)
    @classmethod
    def get_instance(cls, info):
        res = info.split("-")
        return cls(res[0], res[1])

if __name__ == '__main__':
    print("=======classticmethod静态方法演示：=======")
    Message.get_info()
    print("===========init构造方法使用后演示：=========")
    m = Me("百度", "www.baidu.com")
    print(m)
    print("类方法演示")
    m2 = Me.get_instance("谷歌-www.google.com")
    print(m2)
