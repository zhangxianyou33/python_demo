def log_logging(level="info"):
    def wrapper(func):
        def inner(*args, **kwargs):
            #获取包装函数的名称
            print("【logging-{}】的日志，当前函数为：{}".format(level,func.__name__))
            return func(*args, **kwargs)
        return inner # 返回装饰器函数，就是闭包
    return wrapper
class Message:
    @log_logging(level="DEBUG")  # 设置参数
    def print_title(self):
        print("正在使用print——title方法！")

if __name__ == '__main__':
    m = Message()
    m.print_title()

