import calendar

calendar.setfirstweekday(calendar.SUNDAY) #设置一周的开始周几，默认周一

print(calendar.calendar(2021))   # 显示年历
print(calendar.month(2021, 8))   # 显示月历
print(calendar.monthrange(2021, 8)) #返回该年月的：第一天是星期几，一个月的天数【实测不准！！】
print(calendar.isleap(2020))     # 判断是否闰年
print(calendar.leapdays(2012,2020)) #判断俩年份间的闰年个数，包头不包尾
