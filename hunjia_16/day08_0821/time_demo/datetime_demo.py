from datetime import date

print("=======datetime.date日期操作演示===========")
print(date.today())  #获取今天的日期
res = date(2021,9,17)
print(res.weekday())    #获取指定日期，是星期几
print(res.isoformat())  #获取指定日期，格式化

print("=======datetime.time时间操作演示===========")
from datetime import time   # 和time.time模块不能同时导入
from datetime import datetime
from datetime import timedelta
time_str = time(23, 59, 59)
print("获取指定时间为：{}时{}分{}秒".format(time_str.hour, time_str.minute, time_str.second ))
date_res = datetime(2021, 8, 22, 22, 54, 27) #只需要传入年月日时分秒
print("获取指定日期时间：", date_res)
print("=======datetime.timedelta时间操作演示===========")
print("再加X小时，实际日期为：",date_res + timedelta(hours=30))
print("再加上X天，实际日期为：",date_res + timedelta(days=20))
print("再减去X天，实际日期为：",date_res - timedelta(days=20))
print("=======datetime.tzinfo时区演示===========")
from datetime import tzinfo

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
    print("北京时间：", china_date)
    print("德国时间：", gemena_date)
    print("北京转德国时间：", china_date.astimezone(UTC(1)))
    print(china_date - gemena_date)