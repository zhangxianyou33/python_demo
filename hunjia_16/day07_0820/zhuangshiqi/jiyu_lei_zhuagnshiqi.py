# 使用call方法

class logging:
    def __init__(self, level = "INFO"):
        self.__level = level
    def __call__(self, func):
        def inner(*args, **kwargs):
            # 获取包装函数的名称
            print("【logging-{}】的日志，当前函数为：{}".format(self.__level, func.__name__))
            return func(*args, **kwargs)

        return inner  # 返回装饰器函数，就是闭包
class Message:
    @logging(level="DEBUG")
    def print_info(self):
        print("正在使用print_info的方法。")

if __name__ == '__main__':
    m = Message()
    m.print_info()