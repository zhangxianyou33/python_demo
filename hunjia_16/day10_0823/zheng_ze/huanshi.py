# 环视，不是匹配字符串，而是获取字符串位置

import re
info = "id:root,name:tom,age:33,id:root"
mark = r"(?<=id:)(?P<name>\w+)"
print(re.findall(mark, info))