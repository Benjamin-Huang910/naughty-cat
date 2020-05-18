#!/usr/bin/env python
# coding: utf-8

# In[ ]:


d={'acct1':'123','acct2':'456','acct3':'789'}

while True:
    name=input("請輸入您的用戶名: ")
    if name in d:
        break
    else:
        print("您輸入的用戶名不存在，請重新輸入")
        continue
count=3
while count:
    password=input("請輸入您的密碼: ")
    if d[name] == password:
        print("進入系統")
        break
    else:
        count-=1
        print("您輸入的密碼不正確，還有{}次輸入機會".format(count))
        continue
value={'1104':'現金','1121':'應收票據'}
while True:
    func=input("請選擇您欲使用的會計字典功能(查詢/新增/刪除/跳出): ")
    if func == "查詢":
        key=input("請輸入欲查詢的科目代碼")
        if key in value:
            print(value[key])
        else:
            print("查無此科目")
    elif func == "新增":
        key_u=input("請輸入欲新增的代碼")
        value_u=input("請輸入欲新增的科目")
        value[key_u]=value_u
    elif func == "刪除":
        key_d=input("請輸入欲刪除的代碼")
        if key in value:
            del value[key_d]
        else:
            print("無法刪除不存在的代碼")
    elif func == "跳出":
        break
    else:
        print("查無此功能")
file1=open('科目表.txt', 'a+',  encoding='utf-8')
file1.write(str(value))
file1.close()

