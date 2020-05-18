#!/usr/bin/env python
# coding: utf-8

# In[ ]:


count=1
Male_H=[]   #宣告一個空的串列變數名稱為Male_H
Male_W=[]
#透過while迴圈產生串列
print('請依序輸入30個男生的身高以及體重，每輸入完一個身高跟體重後請按Enter，再接著輸入下一個:')
while count<=30:
    line1 = input('輸入第'+str(count)+'個身高:')  #使用者輸入
    line2 = input('輸入第'+str(count)+'個體重:')  #使用者輸入
    if line1.isdecimal():
        data=int(line1)  #資料型態轉換
        Male_H.append(data)  #將data附加到Male_H這個List中
    else:
        print(f"剛剛輸入的第{count:3d}個身高打錯囉，顆顆")
    if line2.isdecimal():
        data=int(line2)  #資料型態轉換
        Male_W.append(data)  #將data附加到Male_W這個List中
    else:
        print(f"剛剛輸入的第{count:3d}個體重打錯囉，顆顆")
    count+=1

print('已完成輸入\n')
print("男生身高:",Male_H)
print("男生體重:",Male_W)
H_bar=sum(Male_H)/len(Male_H)
W_bar=sum(Male_W)/len(Male_W)
H_d=[]
W_d=[]
H_dXW_d=[]
H_dXH_d=[]
for i in range(len(Male_H)):
    h=Male_H[i]-H_bar
    H_d.append(h)
for j in range (len(Male_W)):
    w=Male_W[j]-W_bar
    W_d.append(w)
for k in range(len(Male_H)):
    hw=H_d[k]*W_d[k]
    H_dXW_d.append(hw)
離均差乘積和=sum(H_dXW_d)
for i in range(len(Male_H)):
    q=(Male_H[i]-H_bar)*(Male_H[i]-H_bar)
    H_dXH_d.append(q)
離均差平方和=sum(H_dXH_d)
b1=離均差乘積和/離均差平方和
print(b1)
b0=W_bar-b1*H_bar
print(b0)
print("W(男生)="+str(b0)+"+"+str(b1)+"H(男生)")


# In[ ]:


count=1
Female_H=[]   #宣告一個空的串列變數名稱為Female_H
Female_W=[]
#透過while迴圈產生串列
print('請依序輸入30個女生的身高以及體重，每輸入完一個身高跟體重後請按Enter，再接著輸入下一個:')
while count<=30:
    line1 = input('輸入第'+str(count)+'個身高:')  #使用者輸入
    line2 = input('輸入第'+str(count)+'個體重:')  #使用者輸入
    if line1.isdecimal():
        data=int(line1)  #資料型態轉換
        Female_H.append(data)  #將data附加到Female_H這個List中
    else:
        print(f"剛剛輸入的第{count:3d}個身高打錯囉，顆顆")
    if line2.isdecimal():
        data=int(line2)  #資料型態轉換
        Female_W.append(data)  #將data附加到Female_W這個List中
    else:
        print(f"剛剛輸入的第{count:3d}個體重打錯囉，顆顆")
    count+=1

print('已完成輸入\n')
print("女生身高:",Female_H)
print("女生體重:",Female_W)
H_bar=sum(Female_H)/len(Female_H)
W_bar=sum(Female_W)/len(Female_W)
H_d=[]
W_d=[]
H_dXW_d=[]
H_dXH_d=[]
for i in range(len(Female_H)):
    h=Female_H[i]-H_bar
    H_d.append(h)
for j in range (len(Female_W)):
    w=Female_W[j]-W_bar
    W_d.append(w)
for k in range(len(Female_H)):
    hw=H_d[k]*W_d[k]
    H_dXW_d.append(hw)
離均差乘積和=sum(H_dXW_d)
for i in range(len(Female_H)):
    q=(Female_H[i]-H_bar)*(Female_H[i]-H_bar)
    H_dXH_d.append(q)
離均差平方和=sum(H_dXH_d)
b1=離均差乘積和/離均差平方和
print(b1)
b0=W_bar-b1*H_bar
print(b0)
print("W(女生)="+str(b0)+"+"+str(b1)+"H(女生)"

