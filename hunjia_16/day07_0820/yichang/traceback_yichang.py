import traceback

def main():
    print("=======开始计算========")
    try:
        num = int(input("请输入数字："))
        num2 = int(input("请输入数字："))
        res = num / num2
        print("计算结果为：",res)
    except Exception  as z:
        print("Exception正在处理：", traceback.format_exc())
    finally:
        print("=======执行完毕=======")
if __name__ == '__main__':
    main()
