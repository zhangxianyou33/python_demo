class Message:
    def send(self,info):
        print("消息发送：",info)
class Me:
    def __getattribute__(self, item):
        print("attribute:", item)     #执行拦截的操作
        return object.__getattribute__(self, item) # 放开拦截的操作
    def send(self,info):
        print("消息发送：",info)

class Lanjie:
    def __getattribute__(self, item):
        if item == "content":
            return "这是拦截信息"
        elif item == "send":
            return self.other  # 返回其他方法的引用
        else:
            return object.__getattribute__(self, item)  # 放开拦截
    def send(self,info):
        print("消息发送：",info)
    def other(self, note):
        print("【替换方法】other:", note)

if __name__ == '__main__':
    m = Message()
    print("=============不拦截代码演示：=============")
    m.info="百度一下"
    print(m.info)
    m.send("www.baidu.com")
    print("============拦截代码演示：=============")
    me = Me()
    me.info = "www.google.com"
    print(me.info)   #调用拦截
    me.send("www.google.com")#调用拦截

    #所有的拦截，都是自动完成的
    print("============拦截后替换方法演示：=============")
    lj = Lanjie()
    lj.content = "lanjie的content"
    print(lj.send("www.com"))