# 内置的实现日期的模块，数据类型分为三种
"""
时间戳：1970年，1月1日开始
时间元祖：包含日期，时间，保存日期结构的元祖对象
格式化时间日期：按照指定的标记进行格式化处理
"""
import time_demo
res = time_demo.time()
print(res)  #获取时间戳：1629537871.082874


#时间戳的使用，计算程序执行时间
def sum():
    s = 0
    for i in range(29999999):
        s += i
    return s
def main():
    qidong1 = time_demo.time()
    cpu_time1= time_demo.process_time()
    sum()
    qidong2 = time_demo.time()
    cpu_time2 = time_demo.process_time()
    print("【程序CPU耗时统计】：{}秒".format(cpu_time2-cpu_time1))
    print("【程序计算耗时统计】：{}秒".format(qidong2-qidong1))
main()


