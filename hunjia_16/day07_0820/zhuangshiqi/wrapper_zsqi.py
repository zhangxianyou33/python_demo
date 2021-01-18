#wrapt减少嵌套层数

#先安装：pip install wrapt
import  wrapt
@wrapt.decorator()
def logging(wrapped, insrance, args, kwargs):
    print("【方法一：logging】的日志，当前函数为：{}".format(wrapped.__name__))


def log_log(level="INFO"):
    @wrapt.decorator()
    def log_wrapper(wrapped, insrance, args, kwargs):
        print("【方法二：logging-{}】的日志，当前函数为：{}".format(level,wrapped.__name__))
        return wrapped(*args, **kwargs)
    return log_wrapper

class Message:
    # @logging                #这是方法一
    @log_log(level="DEBUG")   #这是方法二
    def print_info(self):
        print("正在使用print_info的方法")

if __name__ == '__main__':
    m = Message()
    print(m.print_info())
