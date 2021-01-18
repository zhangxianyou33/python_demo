import doctest

#在程序中，对执行部分进行描述，结果部分直接编写
# 坑逼模块，>>> 后面必须留一个空格，不然会报错！！！
def fun(v1, v2):
    """
    >>> fun(5,6)
    30
    >>> fun("he",2)
    'hehe'
    """
    return v1 * v2

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    #True表示，执行时候输出详细信息，默认为False