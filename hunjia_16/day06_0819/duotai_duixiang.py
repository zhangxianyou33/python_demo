# 对象的多态性
# 本质是操作的不确定性，但是不确定性有同意的操作方式


class Message:
    def get_info(self):
        return "Message父类：www.google.com"

class Data(Message):
    def get_info(self):   #方法覆写
        return "Data子类：数据信息"

class Net(Message):
    def get_info(self):
        return "Net子类：网络信息"

class Channel:
    def send(self, msg):
        # print(msg.get_info())  # 统一为get_info的调用
        if isinstance(msg, Message):
            print(msg.get_info())
if __name__ == '__main__':
    c = Channel()
    c.send(Message())
    c.send(Data())
    c.send(Net())
    # 当给send传入的不是类对象，而是字符串就会报错，例如：
    # c.send("hello word")
    #所以需要先判断对象是否为类,修改代码如上
    print(isinstance("hello", Net))
    c.send("hello word")
    #当方法覆写与多态性，结合在一起，只需要在父类中定义需要的方法名称，
