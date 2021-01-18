print("刚安装好pycharm。")
print("使用的环境env：anaconda的环境，3.8版本")

import datetime
print(datetime.datetime)
print("\033[1;31;40m hello word \033[0m")

from mldn.math_demo import add

if __name__ == '__main__':
    add(1,2,3)
    print("累加结果为：",add(1,2,3))


