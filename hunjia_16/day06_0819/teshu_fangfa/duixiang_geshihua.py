#格式化语法很多，也可以自定义格式化对象
# 需要format的方法支持

class Member:
    def __init__(self, title, url):
        self.__title = title
        self.__url = url
    def __format__(self, format_spec):
        if format_spec == "":
            return str(self)
        else:
            format_data = format_spec.replace("%title", self.__title)
            res = format_data.replace("%url", self.__url)
            return res

    def __str__(self):
        return "名称：{}，网站：{}".format(self.__title, self.__url)

class Message_list:
    def __init__(self, msg):
        self.msg = msg
    def __format__(self, format_spec):
        if format_spec == "":
            return str(self)
        else:
            data = "\n".join("{:{fs}}".format(m, fs=format_spec)for m in self.msg)
            return data
if __name__ == '__main__':
    m = Member("谷歌","www.google.com")
    print("未定义格式化：",m)
    print("定义格式化：{info:%title:%url}".format(info = m))

# 自定义格式化，是为了提供更多功能，例如序列
    print("======序列操作演示=====")
    ml = Message_list([Member("百度","www.baidu.com"), Member("搜狐","www.sohu.com")])
    print("{info:%title:%url}".format(info = ml))
