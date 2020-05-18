#!/usr/bin/env python
# coding: utf-8

# In[ ]:


score=0
count=1
grade=[]
print('請輸入學生的分數，每輸入完一個分數後請按Enter，在接著輸入下一個，輸入完畢後請輸入"-1":')
while score!="-1":
    try:
        score=input('輸入第'+str(count)+'個分數:') #使用者輸入
        if score.isdecimal():
            if float(score)<=100 and float(score)>=0:
                data=float(score) #資料型態轉換
                grade.append(data) #將data附加到grade這個list中
                count=count+1
            else:
                print("此數字不在設定的分數範圍內")
        elif float(score)==-1:
            print("輸入完畢\n")
        else:
            print('剛剛輸入的第'+str(count)+'個值並非正整數，故不加入串列中')
    except ValueError:
        print("請輸入對的格式")
average_score=sum(grade)/len(grade)
print("全班的總平均成績為:",average_score)
grade_s=sorted(grade, reverse=True)
print("全班成績的高低排序:",grade_s)


# In[ ]:




