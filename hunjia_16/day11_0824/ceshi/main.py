# 原始的，单个测试代码
from gongnegn_ceshi import func

def main():
    if func(5,6) *3 ==30:
        print("乘法计算ok")
    else:
        print("数学乘法计算失败！")

def main2():
    if func("hello",3) == "hellohellohello":
        print("字符串乘法计算ok")
    else:
        print("字符串乘法计算失败！")
if __name__ == '__main__':
    main()
    main2()