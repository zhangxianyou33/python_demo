def yield_demo():
    print("【yield】代码开始执行")
    res = yield "yield数据"
    print("【yield】代码执行完毕",res)
    yield  res
def func_new():
    res = yield_demo() # 获取生成器对象，内部包含yield
    print("输出生成器对象--默认方法：", res)
    print("============下面为yield方法=========")

    print("输出生成器对象-next方法：", next(res))  #获取返回值
    print("向yield发送数据-send方法：", res.send(8))  #发送数据给yield

func_new()