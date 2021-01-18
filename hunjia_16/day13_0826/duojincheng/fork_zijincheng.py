import os
import multiprocessing as mp

#fork创建的子进程是，不能跨平台的
def child(): #子进程
    print("【child】父进程id：{} ，子进程id：{}".format(
        os.getppid(), os.getpid()))
if __name__ == '__main__':
    def main():
        print("【main】进程id：{}， 进程名称：{}".format(
            mp.current_process().pid, mp.current_process().name
        ))
        #创建子进程
        newpid = os.fork()
        print("新的fork，子进程id：", newpid)
        if newpid == 0:
            child()
        else:
            print("父进程执行中:", os.getpid())
    main()