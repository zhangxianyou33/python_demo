#性能分析，profile，以及cprofile模块

import cProfile
def plu(num):
    s = 0
    for i in range(num):
        s += i
    return s
if __name__ == '__main__':
    # 测试功能函数，后面可定义结果保存位置，文件名
    cProfile.run("plu(9999999)", "f:\\test.result")
"""
ncalls       tottime  percall    cumtime     percall         filename:lineno(function)
函数调用总次数  总运行时间 运行平均时间 总计运行时间  运行一次的平均时间  所在文件名，代码行，函数名
"""