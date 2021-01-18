import time

time_num = time.time()                 # 获取时间戳
time_tuple = time.localtime(time_num)  # 时间戳转为时间元祖
res_res = time.mktime(time_tuple)      # 时间元祖转换回时间戳
format_time= time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  #日期格式化
res_tuple_time  = time.strptime(format_time, '%Y-%m-%d %H:%M:%S')

print("时间戳：",time_num)
print("时间戳转为时间元祖：",time_tuple)
print("时间元祖转为时间戳：",res_res)
print("格式化日期显示：", format_time)
print("格式化时间转回时间元祖：", res_tuple_time)
print("格式化日期显示-只显示日期：", time.strftime("%F", time.localtime()))
print("格式化日期显示-只显示时间：", time.strftime("%T", time.localtime()))
print("格式化日期显示-只显示时间：", time.strftime("%T", time.localtime()))

print("=======内置时间模块===========")
print(time.asctime())
print(time.ctime())
print("获取时间切片：", time.ctime()[11:19])
print([ i for i in    time.ctime()])
