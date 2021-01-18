# 静态方法：类中没有提供任何实例属性，python没有提供静态方法，由装饰器实现
# 类中的静态方法，不需要产生实例化对象可以在没有实例化对象的前提下调用，
# 但是类中的普通方法，必须在实例化对象后才可以调用
# 实际开发中，首选还是普通方法，需要实例化，不需要实例化对象的才使用静态方法。
class Message:
    title = "百度一下"
    # def get_info(self):  #普通方法
    @staticmethod   # 使用内部装饰器
    def get_info():  #类中不带self的，静态方法
        Message().hello()  # 类中的普通方法，必须在实例化对象后才可以调用
        return "www.baidu.com"

    #普通方法，装饰器无法调用，运行直接报错
    def hello(self):   #类中的,带self的普通方法
        print("【hello方法】这是错误调用！")

if __name__ == '__main__':
    print("静态装饰方法：",Message.title, Message.get_info())


