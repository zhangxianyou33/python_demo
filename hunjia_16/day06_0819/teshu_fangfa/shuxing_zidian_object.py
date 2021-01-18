class Message(object):
    def __init__(self, note):
        self.__note = note
class Me:
    def __init__(self, note):
        self.__note = note  # 定义私有属性
    def remove_note(self): #note为属性封装，通过类的内部才可以进行访问
        del self.__note
    def get_note(self):
        return self.__note

    def __setattr__(self, key, value):
        print("【setattr】key={},value={}".format(key, value))
    def __getattr__(self, item):
        print("【getattr】item=", item)
    def __delattr__(self, item):
        print("【del attr】item =", item)

class M:
    def __init__(self, note):
        self.__note = note  # 定义私有属性
    def remove_note(self): #note为属性封装，通过类的内部才可以进行访问
        del self.__note
    def get_note(self):
        return self.__note

    def __setattr__(self, key, value):
        print("【setattr】key={},value={}".format(key, value))
        self.__dict__[key] =  value
    def __getattr__(self, item):
        print("【getattr】item=", item)
        return "{}属性不存在，没有返回值".format(item)
    def __delattr__(self, item):
        print("【del attr】item =", item)
        self.__dict__.pop(item)   # 从字典里面删除属性
if __name__ == '__main__':
    m = Message("note属性")
    m.content = "www.baidu.com"
    print(m.__dict__)
    # 程序中msg实例化对象的两个属性，都保存在dict字典中
    # 设置属性拦截:必须手工设置dict参数数据
    # 获取属性拦截:当属性不存在的时候才会拦截
    # 删除属性拦截:
    #       "setattr, getattr, delattr")
    print("========开始属性监听=========")
    me = Me("www.google.com")
    print("获取存在的属性：", me.get_note())
    print("获取不存在的属性：", me.content)
    me.remove_note()
    print("========属性监听放开=========")
    m = M("www.google.com")
    print("获取存在的属性：", m.get_note())
    print("获取不存在的属性：", m.content)
    m.remove_note()