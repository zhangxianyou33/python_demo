
#明确告诉用户，可能出现的异常
#覆写可能出现的异常提示，raise提示即可
import traceback



def main():
    print("=======开始====================")
    try:
        raise NameError("【raise-Name异常】应该是输入的名字有误。")
    except Exception as e:
        print("这是Exception输出：", e)
        print("=====下面是traceback异常演示=====")
        print(traceback.format_exc())

if __name__ == '__main__':
    main()

