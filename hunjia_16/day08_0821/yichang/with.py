class Message:
    class Connect:
        def build(self):
            print("开始连线好友。。。")
            return True
        def close(self):
            print("已经断开消息链接。")

    def send(self, info):
        try:
            conn = Message.Connect()
            if conn.build():
                print("正在发送消息：", info)
            else:
                print("出问题了。")
        except Exception as e:
            print("消息延迟：", e)
        finally:
            conn.close()
            print("=====通话完成====")

if __name__ == '__main__':
    m  = Message()
    m.send("百度一下")
    m.send("www.baidu.com")
