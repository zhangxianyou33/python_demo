# __slots__属性的使用


class M:
    __slots__ = ("name", "age")# 定义类de实例属性，只能是这俩


if __name__ == '__main__':
    m = M()
    m.name = "tom"
    # m.score = "77"
    print(m.name)
    # print(m.score)
    M.score = "999"
    print(M.score)  # 类可以随意更改属性，然后实例属性才可以调用
    print(m.score)