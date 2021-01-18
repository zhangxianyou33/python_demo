# 需要先导入re模块
import re

#字符串，匹配查找
info = "www  baidu  com"
print("=======字符串自带find方法查找============")
print(info.find("baidu"))
print(info.find("www"))
print("=======re.match方法从头查找==============")
print("从头匹配OK：", re.match("www", info))  # 匹配成功返回match类对象
print("获取从头匹配OK结果：", str(re.match("www", info).span()))  # span获取位置
print("从头不匹配：", re.match("baidu", info))  #不匹配返回None
print("忽略大小写：", re.match("www","WWW.BAIDU.COM", re.IGNORECASE))
print("=======re.search任意位置查找==============")
print("search匹配：",re.search("www",info))
print("search匹配：",re.search("baidu",info))
print("search忽略大小写：", re.search("www","WWW.BAIDU.COM", re.IGNORECASE))

print("=======re.findall全局查找==============")
print("findall匹配：",re.findall("www",info))
print("findall匹配：",re.findall("baidu",info))
print("findall忽略大小写：", re.findall("www","WWW.BAIDU.COM", re.IGNORECASE))

