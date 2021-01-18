# 数据存储，需要编号，例如字典，生成器可以生成编号
# 生成器会有性能问题



# 传统数据生成缺陷演示,编号操作未全部使用，会占用内存
#合适的做法，是需要的时候再生产，而不是全部生成好了再用
def generator(maxnum):
    print("【代码执行前】")
    num = ("数据-{num}".format(num = i)  for i in range(maxnum))
    print("【代码执行后】")
    return num

def yield_demo(maxnum):
    for i in range(maxnum):
        yield "yield数据-{num}".format(num=i)

def func_old():
    for i in generator(5):
        print(i)
def func_new():
    for i in yield_demo(5):
        print(i)

if __name__ == '__main__':
    print("============传统自定义方法=========")
    print("【代码执行前】")
    func_old()
    print("【代码执行后】")

    print("============下面为yield方法=========")
    print("【代码执行前】")
    func_new()
    print("【代码执行后】")

#yield是python的关键字，作用与return相似

