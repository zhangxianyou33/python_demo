def main():
    print("=======开始计算========")
    try:
        num = int(input("请输入数字："))
        num2 = int(input("请输入数字："))
        res = num / num2
        print("计算结果为：",res)
    except ZeroDivisionError as z:
        print("被除数不能为 0：", z)
    except ValueError as v:
        print("你输入的不是数字：", v)
    finally:
        print("=======执行完毕=======")
if __name__ == '__main__':
    main()
    """
    =======开始计算========
    请输入数字：32
    请输入数字：23
    计算结果为： 1.391304347826087
    =======执行完毕=======
    """