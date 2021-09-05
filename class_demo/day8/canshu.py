# 函数中代码需要使用动态参数，就需要给函数传参
def hanshu(name):
    print("你好啊", name)


hanshu("小不点")  # 不传参数会报错，是否需要参数，由开发者自己决定


# 函数中有多个参数时，怕传错参数，就需要关键字参数
def hanshu2(name1, name2, name3,name):
    print("你好啊", name1, name2, name3)
    print(name)
hanshu2("老大", "老二", "老三",88)

def hanshu3(name3, name2, name1,name):
    print("你好啊", name1, name2, name3)
    print(name)
hanshu2("老大", "老二", "老三",88)


