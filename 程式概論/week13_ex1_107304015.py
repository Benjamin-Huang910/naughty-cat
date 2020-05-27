#!/usr/bin/env python
# coding: utf-8

# In[15]:


def triangle(base, height):
    if base > 0 and height > 0:
        value=base*height/2
        return value
    else:
        return -1
result1=triangle(100, 125)
print(result1)
result2=triangle(-123, 20)
print(result2)

