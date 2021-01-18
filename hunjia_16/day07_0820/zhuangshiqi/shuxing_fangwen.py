#优化属性访问

class Message:
    def __init__(self, info):
        self.__info = info
    def set_info(self, info):
        self.__info = info
    def get_info(self):
        return self.__info
    def del_info(self):
        del self.__info

class Me:
    #属性装饰器，简化操作
    def __init__(self,info):
        self.__info = info
    @property
    def info(self):
        return self.__info
    @info.setter  #修改属性，下面方法名，必须和上面保持一致
    def info(self,info):
        self.__info = info
    @info.deleter
    def info(self):
        del self.__info



if __name__ == '__main__':
    m = Message("百度一下")
    print(m.get_info())
    m.set_info("还是谷歌去吧")
    print(m.get_info())
    m.del_info()      #删除info属性
    print("===========property装饰器演示==========")
    me = Me("www.baidu.com")
    print(me.info)  # 直接访问属性
    me.info = "百度一下：www.baidul.com"  #直接修改属性
    print((me.info))
    del me.info     #删除属性