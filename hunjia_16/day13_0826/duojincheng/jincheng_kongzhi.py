import multiprocessing as mp
import time


def send(msg):
    time.sleep(5)
    print("进程id：{}，进程名称：{}".format(
                mp.current_process().pid,
                mp.current_process().name)) #获取当前进程信息

def main1():
    pro = mp.Process(
        target=send,
        args=("www.baidu.com",),
        name="main1，子进程发送中"
    )
    pro.start()
    print("main1，主发送进程id：{}，发送进程名字：{}，信息已发送完毕！！！".format(
        mp.current_process().name,
        mp.current_process().pid
    )) # 主进程的信息，在子进程执行完毕后才会输出

def main2():
    pro = mp.Process(
        target=send,
        args=("www.baidu.com",),
        name="main2，子进程发送中"
    )
    pro.start()
    pro.join()# 子进程强制优先执行
    print("main2，主发送进程id：{}，发送进程名字：{}，信息已发送完毕！！！".format(
        mp.current_process().name,
        mp.current_process().pid
    )) # 主进程的信息，在子进程执行完毕后才会输出
if __name__ == '__main__':
    print("===========主进程优先演示==============")
    main1()
    print("===========强制优先子进程演示============")
    main2()
