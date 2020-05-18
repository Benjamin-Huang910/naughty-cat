#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Method 1
mydict=({'angel':'天使', 'angle':'角度','cat':'貓','dog':'狗'})
while True:
    try:
        print(mydict[input("請輸入要查詢的英文單字: ")])
    except KeyError:
        print("查不到這個英文單字")


# In[6]:


#Method 2
mydict=({'angel':'天使', 'angle':'角度','cat':'貓','dog':'狗'})
question=input("請輸入要查詢的英文單字: ")
print(mydict.get(question,'找不到這個水果對應的值'))


# In[2]:


mydict=({'angel':'天使', 'angle':'角度','cat':'貓','dog':'狗'})
for key in mydict:
    print(key,":",mydict[key])

