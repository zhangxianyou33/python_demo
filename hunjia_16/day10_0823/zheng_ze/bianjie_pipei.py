import re

#有边界符号，表示单边位置
#如没有边界符号，表示任意全局匹配
str = "food hello Food"
pat = "fo[ol][dlk]$"
print("============开始结束匹配==============")
pat22 = "^fo[ol][dlk]"
pat33 = "fo[ol][dlk]"
print("匹配开头：", re.findall(pat, str, re.I))
print("匹配结尾：", re.findall(pat22, str, re.I))
print("匹配不限开头结尾：", re.findall(pat33, str, re.I))
print("============多位简写匹配==============")
input_data = "2020-09-09"
mark = "[0-9]{4}-[0-9]{2}-[0-9]{2}" # 使用{}进行多次匹配
print("生日格式匹配为：", re.match(mark, input_data, re.I))
print("============拆分匹配==============")
info = "hjdfkj3243423.4324324kjkl343435353adf"
mark2 = r"\d+"  #加R表示，这是正则匹配，不加理论上也可以
print(re.split(mark2, info))
score = "119.9"
mark3 = r"^[+-]?\d+(\.\d+)?$"
print(re.match(mark3, score, re.I))
print("============逻辑匹配==============")
tel = "(010)-12343234"
"""
7-8位数字：'\d{7,8}'
前三位区号：\d{3,4}
区号+括号：(\d{3,4})
"""
mark4 = r"((\d{3,4})|(\(\d{3,4}\)-))?\d{7,8}"
print(re.match(mark4, tel))
