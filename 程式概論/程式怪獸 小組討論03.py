#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
number=random.randint(1,100)
answer=0
while answer!=number:
    answer=int(input("請猜一個1-100之間的數字:"))
    if answer>number:
        print("答錯囉~猜小一點的數字吧> <")
    elif answer<number:
        print("哎呀~要不要試試看猜大一點的數字?")
    else:
        print("答對囉!")


# In[ ]:


print('這個程式會印出使用者輸入的起始與結尾數字區間內所有7的倍數')
s1=int(input('請輸入起始數字:'))
s2=int(input('請輸入結尾數字:'))

for i in range(s1,s2+1):
    if(i%7==0): 
        print (f'{i:d}', end=' ')

