# 装饰器，在核心功能上，在不更改原有功能代码的基础上，切面控制，

# 方法四：定义一个装饰器接收操作函数，是由python传递
def log_logging(func):
    def wrapper(*args, **kwargs):
        #获取包装函数的名称
        print("方法四：这是装饰器的日志方法，当前函数为：{}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper # 返回装饰器函数，就是闭包
class Message:
    @log_logging
    def print_title(self):
        print("方法一：这是print方法直接输出的日志")
        logging()
        log()

#方法二：定义一个日志函数
def logging():
    print("方法二：这是使用logging函数，输出的日志！！")

#方法三：使用inspet模块方法，获取方法名称
def log():
    import inspect
    res = inspect.stack()[1][3]
    print("方法三：这是使用inspect模块，输出的日志！当前方法为：{}".format(res))


if __name__ == '__main__':
    m = Message()
    m.print_title()
