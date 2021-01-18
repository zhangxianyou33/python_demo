class Message:
    def __init__(self):
        self.__mlist = ["百度", "阿里", "腾讯"]
    def get_list(self):
        return self.__mlist
    def __reversed__(self):
        self.__mlist = reversed(self.__mlist)

if __name__ == '__main__':
    m = Message()
    print("下面是自定义的反转操作：")
    reversed(m)

    for i in m.get_list():
        print(i, end=",")