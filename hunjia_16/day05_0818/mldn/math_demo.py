def add(*numbers):
    """
    实现数字累加
    :return:累加结果
    """
    s = 0
    for i in numbers:
        s += i
    return s
