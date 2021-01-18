# 内部类的，嵌套，实现特定的类服务


class Message:
    def send(self, msg):
        conn = Message.Connect()  # 内部类名称=外部类。内部类

        if conn.build():
            print("发送消息：", msg)
            conn.close()
        else:
            print("消息发送失败，无法进行链接")


    class Connect:   #内部类是为了外部类服务的
        def build(self):
            print("connect链接中，发送消息中")
            return True
        def close(self):
            print("connect关闭中，断开链接")

# 对以上俩类进行简写如下
class Outer:
    def __init__(self):
        self.__info = "www.google.com"
    def get_info(self):
        return self.__info
    class __Inner:
        def __init__(self,out):
            self.__out = out
        def pint_info(self):
            print(self.__out.get_info())
    def fun(self):
        inobj = Outer.__Inner(self)  # 实例化颞部类对象

#在方法中，定义内部类
class F():
    def __init__(self):
        self.__info = ":www.sohu.com"
    def print_info(self, title):
        print(title, self.__info)
    def fun(self, msg):
        obj = self
        subtitle = "软件学院"
        class Inner:
            def send(self):
                obj.print_info(msg + subtitle)
        Inner().send()


if __name__ == '__main__':
    m =Message()
    m.send("百度")
    print("外部使用内部类===========")

    conn = Message.Connect()
    print(conn.build())
    print("内部类封装：加__,__Connect,外面就访问不了，只允许被Message类使用")

    out = Outer()
    out.fun()

    print("下面是在方法中，定义外部类：")
    f = F()
    f.fun("科技兴国,")
#以上方法等同于一下两个类的 方法
# class Message:
#     def send(self, msg):
#         print("发送消息：", msg)
#
#
# class Connect(Message):   #内部类是为了外部类服务的
#     def build(self):
#         print("connect链接中，发送消息中")
#         return True
#     def close(self):
#         print("connect关闭中，断开链接")
#
# if __name__ == '__main__':
#     m =Connect()
#     if m.build():
#         m.send("百度一下")
#         m.close()
#     else:
#         print("发送消息失败!")
#         m.close()