# 一个子类继承多个父类的内容

class Message:
    def send(self, msg):
        print("消息发送中：", msg)

class Connect:
    def build(self):
        print("Connect：正在链接服务器中")
        return True
    def close(self):
        print("处理完毕,断开链接了！！！")


class Net(Message, Connect):
    def net(self, msg):
        if self.build():
            self.send(msg)
            self.close()
        else:
            print("哎，连接不到服务器")



if __name__ == '__main__':
    n = Net()
    n.net("你好啊,很高兴认识你。")