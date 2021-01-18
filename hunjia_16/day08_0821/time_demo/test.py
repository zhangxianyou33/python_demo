from datetime import tzinfo
from datetime import datetime
from datetime import timedelta


# 继承tzinfo,覆写方法
class UTC(tzinfo):
    def __init__(self, offset=0):
        self.__offset = 0
    def tzname(self, dt):
        return "UTC时区：".format(self.__offset)
    def utcoffset(self, dt):
        return timedelta(hours=self.__offset)
    def dst(self, dt):
        return timedelta(hours=self.__offset)
if __name__ == '__main__':
    china_date = datetime(2021, 8, 22, 22, 54, 27, tzinfo=UTC(8))
    gemena_date = datetime(2021, 8, 22, 22, 54, 27, tzinfo=UTC(1))
    print("=======datetime.tzinfo时区演示===========")
    print("北京时间：", china_date)
    print("德国时间：", gemena_date)
    print("北京转德国时间：", china_date.astimezone(UTC(1)))
    print(china_date - gemena_date)