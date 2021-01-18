# 定义可用数据的范围

import enum

@enum.unique  #使用装饰器，防止数据重复，如果重复，运行就会报错：duplicate values

class Color_Base(enum.Enum):  # 必须强制继承父类
    red = 0
    green = 1
    blue = 2

if __name__ == '__main__':
    c = Color_Base.blue  # 直接通过枚举，获取所需要的一个对象
    print("枚举对象名称：{}，枚举对象类型：{}".format(c.name, c.value))
