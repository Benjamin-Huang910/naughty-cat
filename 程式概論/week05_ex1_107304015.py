#!/usr/bin/env python
# coding: utf-8

# In[2]:


instruction="請輸入您的額溫"
print(instruction)
C=1
while float(C)>0:
    C=input(">> ")
    if float(C)>=36.5 and float(C)<=37.5:
        print("體溫正常")
    elif float(C)>37.5:
        print("體溫過高!")
    elif float(C)<36.5 and float(C)>0:
        print("體溫過低!")
    else:
        print("結束")

