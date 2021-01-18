#正则匹配模式
import re

data = """    
food is very good
food is very good
food is very good    
"""
mark = "fo{2}d"
mark2 = ".+"
print("多行匹配以及忽略大小写：",re.findall(mark, data, re.I  | re.M)) #多行匹配以及忽略大小写
print("默认匹配，不加其他后缀：",re.findall(mark2, data)) #多行匹配以及忽略大小写
print("修改.匹配任意模式，可匹配换行等任意字符：",re.findall(mark2, data, re.S)) #多行匹配以及忽略大小写
print("忽略空白和注释，进行匹配：",re.findall(mark2, data, re.X)) #多行匹配以及忽略大小写
