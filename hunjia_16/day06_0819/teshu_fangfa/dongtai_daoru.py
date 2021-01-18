# import 类似，实现模块的动态导入

# 传统的做法是导入后，调用
# 不适用import语句,基于对象的动态导入

def main():
    util = __import__("util")
    get_info_obj = getattr(util, "get_info")
    print(get_info_obj())
    message_class = getattr(util, "Message")
    print(message_class().echo("www.baidu.com"))
if __name__ == '__main__':
    main()