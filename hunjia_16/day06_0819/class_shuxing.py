# 类属性，实例属性

# 实例和类属性，都可以动态增加
# 开发中，优先使用实例属性，
# 描述公共信息优先使用类属性

class M:
    info = "baidu.com"



if __name__ == '__main__':
    print(M.info)
    m = M()
    m.name = "属性"
    print(m.name)
    m.info = "hello"
    print("下面的俩属性重名了：")
    print(m.info)
    print(M.info)
    print("在外面增加属性,实例属性会继承")
    M.url = "www.google.com"
    print(m.url)