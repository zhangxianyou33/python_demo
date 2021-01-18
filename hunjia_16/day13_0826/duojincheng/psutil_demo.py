#psutil是进程管理的，第三方模块，可以跨平台使用
import time

import psutil

#获取进程信息
for i in psutil.process_iter():
    print("进程编号：{}， 进程名称：{}， 创建时间：{}".format(
        i.pid, i.name(), time.ctime( i.create_time())[11:20]
    ))


#获取CPU信息
print("获取CPU的数量：", psutil.cpu_count(logical=False))
print("获取CPU的逻辑数量：", psutil.cpu_count(logical=True))
print("用户CPU的使用时间：", psutil.cpu_times().user)
print("系统CPU的使用时间：", psutil.cpu_times().system)
print("CPU的空闲时间：", psutil.cpu_times().idle)
for i in range(10):
    print("cpu使用监控：", psutil.cpu_percent(interval=1,percpu=True))


# 获取磁盘的使用情况
print("获取磁盘信息：", psutil.disk_partitions())
print("获取磁盘使用率：", psutil.disk_usage("c:"))
print("获取磁盘io使用率：", psutil.disk_io_counters())

#获取网络信息
print("网络交互信息,数据统计：", psutil.net_io_counters())
print("网络交互信息，接口统计：", psutil.net_if_addrs())
print("网络交互信息，接口状态：", psutil.net_if_stats())