class Message:
    def send(self, msg):
        print("发送消息：", msg)


class Connect(Message):   #内部类是为了外部类服务的
    def build(self):
        print("connect链接中，发送消息中")
        return True
    def close(self):
        print("connect关闭中，断开链接")

if __name__ == '__main__':
    m =Connect()
    if m.build():
        m.send("百度一下")
        m.close()
    else:
        print("发送消息失败!")
        m.close()