#方法一：使用系统内置函数open
def open_file():
    try:
        file = open(r"test.txt", "r")
        print("文件名称：",file.name)
        print("文件是否已关闭：",file.closed)
        print("文件访问模式：", file.mode)
    finally:
        file.close()
        print("使用close方法，关闭文件状态为：", file.closed)
open_file()

print("======open方法，写入文件======")
def open_write():
    try:
        f = open("test.txt", "w")
        f.write("这是使用open，写入的文件\nhello word\n第三行\n")

    finally:
        f.close()
open_write()

print("======使用with方法，读取文件======")
def with_read():
    with open(r"test.txt", "r") as file:
        data = file.readline()
        while data:
            print(data, end="")
            data = file.readline()
with_read()
#方法二：使用with方法
print("======使用with方法，写入文件======")
def with_write():
    with open("test.txt", "w") as f:
        f.write("使用with的write方法，写入文件，旧的文件已经被覆盖\n")
with_write()


with_read()

print("======使用with方法追加文件======")
def with_add():
    with open("test.txt", "a") as f:
        f.write("这是with的追加文件！！！\n")
with_add()

with_read()

print("======使用with方法，迭代读取文件======")
def for_read():
    with open("test.txt", "r") as f:
        for i in f:
            print(i, end="")
for_read()