# with关键词，管理上下文，上下文开启，上下文退出

class Message:
    class Connect:
        def build(self):
            print("开始连线好友。。。")
            return True
        def close(self):
            print("已经断开消息链接。")
    def __enter__(self):
        print("=====with语句开始执行=====")
        self.conn = Message.Connect()
        if not self.conn.build():
            print("建立通话失败。")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("=====with语句结束了=======")
        self.conn.close()
    def send(self, info):
        print("正在发送消息：", info)

if __name__ == '__main__':
    with Message() as me:
        me.send("谷歌")
        me.send("www.google.com")
