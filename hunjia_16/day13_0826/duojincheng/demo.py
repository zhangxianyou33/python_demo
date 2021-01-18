# 早期的CPU是单核：实现多个程序并行，在某一时间点，其实只有一个进程
# 后来硬件多核CPU：多个进程是并行执行。

from multiprocessing import cpu_count

print("CPU内核数量：", cpu_count())
"""
生命周期为：
1.分配pcb
2.获得山下文资源，等待CPU
3.CPU已获得，开始执行
4.如遇到无法执行，进入阻塞状态
5.到达自然结束点或者意外终结，进入终止状态
"""