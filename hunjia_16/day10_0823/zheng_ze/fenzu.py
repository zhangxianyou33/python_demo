#获取数据后，需要再拆分，可以使用分组
import re

info = "id:root, phone:11012341234, bir:2021-09-08"
mark = r"(\d{4})-(\d{2})-(\d{2})"
res = re.search(mark, info)
print("获取分组数据为 ：", res.group())
print("获取第1组数据为：", res.group(1))
print("获取第2组数据为：", res.group(2))
print("获取第3组数据为：", res.group(3))
mark2 = r"\d{4}-\d{2}-\d{2}"
res2 = re.search(mark2, info)
print("不加分组括号为 ：",res2.group())

