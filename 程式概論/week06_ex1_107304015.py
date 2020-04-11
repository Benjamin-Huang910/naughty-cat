#!/usr/bin/env python
# coding: utf-8

# In[1]:


height=input("請輸入身高(cm): ")
weight=input("請輸入體重(kg): ")
BMI=float(weight)/(float(height)/100)**2
print("你的BMI為{:.2f}".format(BMI))
if BMI<18.5:
    print("體重過輕")
elif BMI>=18.5 and BMI<24:
    print("體重正常")
else:
    print("體重過重")
gender=input("請輸入性別(男生/女生): ")
chest=input("請輸入胸圍(cm): ")
if gender=="女生":
    if float(chest)<84:
        print("lativ S")
    elif float(chest)>=85 and float(chest)<89:
        print("lativ M")
    elif float(chest)>89:
        print("lativ L")
    if float(chest)<=82:
        print("UNIQLO S")
    elif float(chest)>82 and float(chest)<=92:
        print("UNIQLO M")
    elif float(chest)>92:
        print("UNIQLO L")
    if float(chest)<84.5:
        print("H:CONNECT S")
    elif float(chest)>=84.5 and float(chest)<88.5:
        print("H:CONNECT M")
    elif float(chest)>88.5:
        print("H:CONNECT L")
    if float(chest)<=88:
        print("H&M S")
    elif float(chest)>88 and float(chest)<=96:
        print("H&M M")
    elif float(chest)>96:
        print("H&M L")
    if float(chest)<=99:
        print("GAP S")
    elif float(chest)>99 and float(chest)<=104:
        print("GAP M")
    elif float(chest)>104:
        print("GAP L")
if gender=="男生":
    if float(chest)<93:
        print("lativ S")
    elif float(chest)>=93 and float(chest)<99:
        print("lativ M")
    elif float(chest)>99:
        print("lativ L")
    if float(chest)<=104:
        print("UNIQLO S")
    elif float(chest)>104 and float(chest)<=116:
        print("UNIQLO M")
    elif float(chest)>116:
        print("UNIQLO L")
    if float(chest)<85:
        print("H:CONNECT S")
    elif float(chest)>=85 and float(chest)<87:
        print("H:CONNECT M")
    elif float(chest)>87:
        print("H:CONNECT L")
    if float(chest)<=88:
        print("H&M S")
    elif float(chest)>88 and float(chest)<=96:
        print("H&M M")
    elif float(chest)>96:
        print("H&M L")
    if float(chest)<=112:
        print("GAP S")
    elif float(chest)>112 and float(chest)<=117:
        print("GAP M")
    elif float(chest)>117:
        print("GAP L")
    


# In[ ]:




