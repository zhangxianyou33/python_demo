# try-except-else-finally

#try----else----  会一起执行
#finally无论如何，最后都会执行
def main():
    try:
        res = 10/0
        print("开始执行计算：",res)
    except ZeroDivisionError as z:
        print("代码执行有误：",z)
    # except TypeError as z:
    #     print("代码执行有误：",z)
    else:
        print("else被执行了====")
    finally:    #不管前面如何，finally一定会执行！
        print("不管是否计算，程序已经执行完毕！")

if __name__ == '__main__':
    main()