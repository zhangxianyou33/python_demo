import multiprocessing
import time


def worker(count):  # 专门的处理函数
    for i in range(count):
        print("{}=进程id为：{}， 进程名字为：{}".format(i,
               multiprocessing.current_process().pid,
               multiprocessing.current_process().name))
        time.sleep(1)  #减慢代码执行速度
def main():
    print("主进程id为：{}， 进程名字为：{}".format(
                multiprocessing.current_process().pid,
                multiprocessing.current_process().name))
    time.sleep(1)
if __name__ == '__main__':
    print("==============主进程===============")
    main()
    print("==============子进程===============")

    for i in range(3):
        #开始创建进程对象
        pro = multiprocessing.Process(
            target=worker,
            args=(10,),
            name="测试进程{}：".format(i))
        pro.start()  # 执行进程启动

"""
python程序都是通过主进程开始的，而后通过Process定义的进程都属于子进程
"""