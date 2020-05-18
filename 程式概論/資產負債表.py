#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1 輸入資料
while True:
    while True:
        cash=input("請輸入現金: ")
        if float(cash) < 0:#2 防呆機制
            print("輸入的資料不合規格，請重新輸入")
            continue
        else:
            break
    while True:
        inventory=input("請輸入存貨: ")
        if float(inventory) < 0:
            print("輸入的資料不合規格，請重新輸入")
            continue
        else:
            break
    while True:
        land=input("請輸入土地: ")
        if float(land) < 0:
            print("輸入的資料不合規格，請重新輸入")
            continue
        else:
            break
    while True:
        equipment=input("請輸入設備: ")
        if float(equipment) < 0:
            print("輸入的資料不合規格，請重新輸入")
            continue
        else:
            break
    while True:
        note_payable=input("請輸入應付票據: ")
        if float(note_payable) < 0:
            print("輸入的資料不合規格，請重新輸入")
            continue
        else:
            break
    while True:
        accounts_payable=input("請輸入應付帳款: ")
        if float(accounts_payable) < 0:
            print("輸入的資料不合規格，請重新輸入")
            continue
        else:
            break
    while True:
        bonds_payable=input("請輸入應付公司債: ")
        if float(bonds_payable) < 0:
            print("輸入的資料不合規格，請重新輸入")
            continue
        else:
            break
    while True:
        retained_earnings=input("請輸入保留盈餘: ")
        if float(retained_earnings) < 0:
            print("輸入的資料不合規格，請重新輸入")
            continue
        else:
            break
    asset=float(cash)+float(inventory)+float(land)+float(equipment)
    liability=float(note_payable)+float(accounts_payable)+float(bonds_payable)
    equity=float(retained_earnings)
    print("資產:",asset)
    print("負債:",liability)
    print("權益:",equity)
    if asset==liability+equity: #3 檢查是否符合會計平衡
        break
    else:
        print("不符合會計平衡，請重新輸入資料")
        continue  
current_asset=float(cash)+float(inventory)
noncurrent_asset=float(land)+float(equipment)
current_liability=float(note_payable)+float(accounts_payable)
noncurrent_liability=float(bonds_payable)
財務結構=liability/asset #4 輸入資料分析「財務結構」、「償債能力」
償還能力=current_asset/current_liability
print("A公司、資產負債表、二○一九年十二月三十一日") #5 印出資產負債表表頭、該年負債佔資產比率、流動比率
print("負債佔資產比率:",財務結構)
print("流動比率:",償還能力)

