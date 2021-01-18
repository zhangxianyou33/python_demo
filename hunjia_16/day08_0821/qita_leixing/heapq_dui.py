# 堆是基于二叉树实现的。最大特点是里面的数据是有序的，同时是中序遍历获取
# 堆中存放的内容，基于二叉树存储，可以方便的实现排序后的数据获取
import heapq

def f():
    data = list(range(10))
    print("定义列表：", data)
    heapq.heapify(data)   # 基于迭代对象创建一个堆
    heapq.heappush(data, 0)# 进行数据的保存
    print("原始堆数据：", data)  #自动对原列表进行更新
    print("获取堆中前2个最大数据：", heapq.nlargest(2, data))
    print("获取堆中前3个最xiao数据：", heapq.nsmallest(3, data))


f()