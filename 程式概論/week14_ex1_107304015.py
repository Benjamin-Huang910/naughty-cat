#!/usr/bin/env python
# coding: utf-8

# In[15]:


#1
def check_float(num):
    try:
        result = float(num)
    except:
        result = False
                           #有發生例外時，將變數result的內容設為False
    else:
        result = True
                           #沒有發生例外時，將變數result的內容設為True
    finally:
        return result
                           #不管有沒有發生例外，最後都將result的內容回傳


while True:
    a=input('輸入一個可以成功轉為浮點數的資料:')
    if (not check_float(a)):
        print('輸入資料有錯誤，請重新', end='')
        continue
    else:
        print('輸入的資料可以成功轉為浮點數', float(a))
        break


# In[ ]:


#2
def check_int(num):
    try:
        result = int(num)
    except:
        result = False
    else:
        result = True
    finally:
        return result
#3
while True:
    a=input('輸入一個可以成功轉為浮點數的資料:')
    if (not check_int(a)):
        print('輸入資料有錯誤，請重新', end='')
        continue
    else:
        print('輸入的資料可以成功轉為浮點數', int(a))
        break

