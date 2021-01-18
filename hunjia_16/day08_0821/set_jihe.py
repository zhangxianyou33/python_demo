# set的交并补集，需要注意前后顺序，前后位置不同，结果不同
# 列表：存储功能，迭代处理 ， 字典：查询功能， 集合：集合运算
def m():
    s1 = set("abcd")
    s2 = set("abxy")
    print("交集符号：", s1 & s2)
    print("交集方法：", s1.intersection(s2))
    print("差集符号：", s1 - s2)
    print("差集符号：", s1.difference(s2))
    print("并集符号：", s1 | s2)
    print("并集符号：", s1.union(s2))
    print("对称差集符号：", s1 ^ s2)   # 和zip函数很像，，感觉没意义
    print("对称差集符号：", s1.symmetric_difference(s2))

m()
