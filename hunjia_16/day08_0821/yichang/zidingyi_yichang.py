#异常类不够使用，所以需要自定义异常
class BugException(Exception):
    def __init__(self, info):
        self.info = info
    def __str__(self):
        return  self.info

class Fun:
    @staticmethod
    def f(num):
        if num > 999:
            raise BugException("哎，不知道哪里出bug了。。")
        else:
            print("目前还没有问题，可以继续运行代码。")
if __name__ == '__main__':
    try:
        Fun.f(1111)
    except BugException as b:
        print("【BugException】异常处理：", b)

