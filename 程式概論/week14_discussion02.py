#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
import time
import calendar
year = list(time.localtime())
year = year[0]
calendar.prcal(year)
#2
import random
month = random.randint(1,12)
calendar.prmonth(year,month)
#3
list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
ransample=random.sample(list1, 4)
for i in ransample:
    print(calendar.month_name[i])

