#!/usr/bin/env python
# coding: utf-8

# In[ ]:


student=15
grade=[] #宣告一個空的串列變數名稱為student
#透過for迴圈產生串列
print('請依序輸入15個分數，每輸入完一個分數後請按Enter，在接著輸入下一個:')
for item in range(student): #range產生的整數有0,1,2,3,4,...,14
    line=input('輸入第'+str(item+1)+'個分數:') #使用者輸入
    if line.isdecimal():
        if int(line)<=100 and int(line)>=0:
            data=int(line) #資料型態轉換
            grade.append(data) #將data附加到grade這個list中
        else:
            print("此數字不在設定的分數範圍內")
    else:
        print('剛剛輸入的第'+str(item+1)+'個值並非正整數，故不加入串列中')
print('已完成輸入\n')
print("輸入的成績有",end='-->\n')
for i in grade:
    print(i,end='\n')
average_score=sum(grade)/len(grade)
print("全班的總平均成績為:",average_score)


# In[ ]:




