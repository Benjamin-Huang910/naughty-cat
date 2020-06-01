#Programming 101
#week14
#demo 6

import calendar

print(calendar.calendar(2019)) #印出2019年的日曆
print(calendar.month(2019,6))  #印出2019年6月的日曆

calendar.prcal(2019)           #印出2019年的日曆，效果等於print搭配calendar()
calendar.prmonth(2019,6)      #印出2019年6月的日曆，效果等於print搭配month()


print(calendar.isleap(2019))   #2019是否為閏年

print(calendar.leapdays(2000,2019)) #2000~2019年之間有幾個閏年

#calendar.month_name裡面有12個月份的英文名稱，但需要透過索引值1~12去個別取出
print(calendar.month_name)  
for i in range(1,13):       #印出1月到12月的英文名稱
    print (calendar.month_name[i])


