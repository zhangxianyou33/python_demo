#编写代码过程中的异常
#异常之间是，继承的关系，所有的异常，父类异常是：Exception
#当不知道会出现何种异常的时候，可以使用


def main():
    print("=======开始计算========")
    try:
        num = int(input("请输入数字："))
        num2 = int(input("请输入数字："))
        res = num / num2
        print("计算结果为：",res)
    except Exception  as z:
        print("Exception正在处理：", z)
    finally:
        print("=======执行完毕=======")
if __name__ == '__main__':
    main()
