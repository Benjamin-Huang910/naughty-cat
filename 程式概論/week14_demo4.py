#Programming 101
#week14
#demo 4

import random

#1 choice()
list1=[78,56,42,92,10,35,12]
print(random.choice(list1))  #從串列list1中隨機挑選一個元素

#2 shuffle()
random.shuffle(list1)    #把串列list1裡面的元素順序打亂
print(list1)

#3 sample()
ransample=random.sample(list1, 3)  #從list1中隨機選三個不重複的元素
print(ransample)   #回傳值為一個串列

#4 random()
r=random.random()   #隨機產生一個0~1之間的浮點數
print(r)

#5 uniform()
y=random.uniform(1,5)    #隨機產生一個1~5之間的浮點數
print(y)

#6 randrange()
x=random.randrange(10,101,2)    #隨機產生一個10~100間的偶數
print(x)

#7 randint()
z=random.randint(1,20)          #隨機產生一個1~20間的整數
print(z)
