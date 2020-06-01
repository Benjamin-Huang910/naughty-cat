#Programming 101
#week14
#demo 5

import time

sec_time=time.time()  #以浮點數回傳從1970/1/1之後到目前的秒數值
print(sec_time)

str_time=time.ctime(sec_time) #以字串表示傳入的秒數所代表的時間
print(str_time)

#取得目前時間
print(time.ctime())     #以time.time()回傳的秒數為基準
print(time.asctime())   #以當地時間localtime()為基準

#時間結構
print(time.localtime())  #當地時間
print(time.gmtime())     #UTC時間
lt=list(time.localtime())  #將時間結構轉為串列
gmt=tuple(time.gmtime())   #將時間結構轉為tuple
print(lt)
print(gmt)


time.sleep(5)   #讓程式執行暫停5秒

pt=time.process_time() #程式開始執行到現在所經過的秒數，但不包括sleep()所用掉的時間
print(pt)

spendtime=time.perf_counter() #程式開始執行到現在所經過的秒數
print(spendtime)

print(time.strptime("30 Nov 20", "%d %b %y")) #將字串轉為時間結構
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
#將時間結構轉為字串，格式代碼請參考https://docs.python.org/3/library/time.html
