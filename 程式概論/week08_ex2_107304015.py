#!/usr/bin/env python
# coding: utf-8

# In[9]:


#1
list_ex=list(range(0,101,2))
print(list_ex,end="")
#2
del list_ex[-5:]
print(list_ex)
#3
str_classtime='15:10:00'.split(':')
list_classtime=str_classtime
print(list_classtime)
#4
list_ex[0]=list_classtime[0]
list_ex[1]=list_classtime[-1:]
print(list_ex)
#5
print('Type of olist_ex:',type(list_ex))
print('Type of olist_ex[0]:',type(list_ex[0]))
print('Type of olist_ex[1]:',type(list_ex[1]))
print('Type of olist_ex[2]:',type(list_ex[2]))

