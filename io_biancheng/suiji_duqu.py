"""
当需要读取的文件位置在文件中间，或者后半半部分，就需要随机读取

"""
name = ("zhangsan","lisa","wangwu")
age = (33,11,22)
def main():
    with open("test2.txt","a") as f:
        for i in range(len(name)):
            content = "{name:<10}{age:>4}\n".format(name=name[i], age=age[i])
            f.write(content)
main()

def read():
    with open("test2.txt", "r") as f:
        f.seek(15)  #指定开始位置，第一行：0，第三行：30
        print("第二行数据：{}, 姓名：{}， 年龄：{}".format(
            f.tell(),
            f.read(10).strip(),
            int(f.read(5))))
read()

name_length = 10
read_length = 5
line_count = 0
def yield_read():
    seek_offset = 0
    with open("test2.txt", "r") as f:
        while True:
            f.seek(seek_offset + name_length)
            data = f.read(read_length)
            if data:
                global line_count
                line_count += 1
                seek_offset = f.tell()
                yield int(data)  #局部返回
            else:
                return
num = 0
for i in yield_read():
    num +=  i
print("一共读取了：{}行信息，用户平均年龄为：{}".format(line_count, num / line_count))
