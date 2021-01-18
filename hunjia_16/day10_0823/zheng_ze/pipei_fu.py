import re

info = "www.baidu.com.17745674567.127.o.0.1.hello.heLLo.heLlo"
print("原始字符串：",info)
print("==========范围内匹配==========")
mark1 = "he[lkn][lkn]o"
mark2 = "he[a-z][a-z]o"
mark3 = "he[a-zA-Z][a-zA-Z]o"

print("匹配[lkn]范围字符：",re.findall(mark1, info, re.I))
print("匹配[a-z]范围字符：",re.findall(mark2, info, re.I))
print("匹配[a-zA-Z]范围字符：",re.findall(mark3, info, re.I))
print("匹配[0-9]范围字符：",re.findall("[0-9]", info, re.I))
print("匹配[^0-9a-t]范围取反匹配：",re.findall("[^0-9a-t]", info, re.I))