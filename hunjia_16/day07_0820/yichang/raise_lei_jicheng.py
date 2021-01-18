class Message:
    def build(self): #如果使用父类的build方法，会报错
        raise NotImplementedError("【Message类】build方法，正在使用。")
class Me(Message):
    def build(self):
        print("【Me子类】build方法，已经覆写。")


if __name__ == '__main__':
    m1 = Message()
    m1.build()

