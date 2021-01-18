# 守护进程，随主进程进行

import multiprocessing
import time


#创建守护进程
def status():
    item = 1
    while True:
        print("守护进程id：{}， 守护进程名字：{}======{}".format(
            multiprocessing.current_process().pid,
            multiprocessing.current_process().name,item
        ))
        item += 1
        time.sleep(1)
#工作进程函数
def worker():
    shouhu_pro = multiprocessing.Process(target=status, name="守护进程", daemon=True)
    shouhu_pro.start()
    for i in range(10):
        print("工作id：{}， 工作进程：{}".format(
            multiprocessing.current_process().pid,
            multiprocessing.current_process().name
        ))
        time.sleep(1)
if __name__ == '__main__':
    def main():
        work_pro = multiprocessing.Process(target=worker, name="工作进程")
        work_pro.start() #启动工作进程
    main()
