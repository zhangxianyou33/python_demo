def fun():
    try:
        raise NameError("【NameError】名称可能异常。")
    except Exception as e:
        print("【Exception】你的代码出bug啦。")
        raise TypeError("TypeError:可能是类型错误。") from e
        # raise TypeError("TypeError:可能是类型错误。") from None
        # from None就找不到源头
if __name__ == '__main__':
    try:
        fun()
    except Exception as e:
        #抛出异常原因
        print("Exception-main{}:运行程序，出现异常原因为:{}".format(e, e.__cause__))