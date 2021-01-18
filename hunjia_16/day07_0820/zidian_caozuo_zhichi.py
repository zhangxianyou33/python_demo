#字典获取为key,value,以及字典【】
 # 与字典的操作一致


class Message:
    def __init__(self):
        self.__map = {}
    def __setitem__(self, key, value):
        print("【set item】设置数据:key={}, value={}".format(key, value))
        self.__map[key] = value
    def __getitem__(self, item):
        print("【get item】获取数据:item=", item)
        return self.__map[item]
    def __len__(self):
        return len(self.__map)
    def __delitem__(self, key):
        print("【del item】马上删除数据:item=", key)
        self.__map.pop(key)
if __name__ == '__main__':
    m = Message()
    print("=====设置数据======")
    m["百度"] = "www.baidu.com"
    print("=====查询获取======")
    print(m["百度"])
    print("=====获取个数======")
    print("获取元素个数：", len(m))
    print("=====删除======")
    del m["百度"]
