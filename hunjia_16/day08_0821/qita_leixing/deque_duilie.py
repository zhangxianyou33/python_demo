# 队列就是，类似于排队办理业务形式，先进先出的原则

#单端队列演示
#双端队列，就是生产消费者模式，依赖collections模块

from collections import deque

def main():
    info = deque(("hello", "word"))  # 内部是序列
    info.append(("百度一下"))          # 右边添加数据
    info.appendleft("www.baidu.com")  # 左边添加数据
    print("【队列数据】：",info)
    print("----开始弹出数据------")
    print(info.pop())
    print(info.popleft())
    print("------弹出完毕--------")
    print(info)

main()