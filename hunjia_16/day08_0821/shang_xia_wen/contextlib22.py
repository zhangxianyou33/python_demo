from contextlib import contextmanager,closing
class Connect:
    def __init__(self):
        print("connect：开始建立连接")
    def send(self, info):
        print("消息发送中")
    def close(self):
        print("connect：关闭网络连接")


if __name__ == '__main__':
    with closing(Connect()) as c:   #自动关闭功能支持
        print("消息发送：www.baidu.com")

"""
消息发送：www.baidu.com
connect：关闭网络连接
"""
