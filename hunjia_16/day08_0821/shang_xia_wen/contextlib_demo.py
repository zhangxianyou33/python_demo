# 使用contextlib模块，进行上下文管理

from contextlib import contextmanager
class Message:
    def send(self, info):
        print("消息发送中")
@contextmanager
def message_wrap():
    class __Connect:
        def build(self):
            print("connect：建立网络连接")
            return False

        def close(self):
            print("connect：关闭网络连接")
    try:
        conn = __Connect()
        if conn.build():
            yield Message()  #获取下一个实例

        else:
            yield None
    except Exception as e:
        print("except连接异常：", e)
    finally:
        conn.close()
if __name__ == '__main__':
    with message_wrap() as m:
        m.send("www.baidu.com")