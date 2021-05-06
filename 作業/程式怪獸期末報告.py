#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random as r
import time


# In[ ]:


# 樂透
def lottery():
    player_choice=[] #玩家樂透數字存放區
    count=3 #輸入3次
    print("請輸入3個1~10的樂透數字以及一個特別獎數字")
    while count != 0:
        try:
            choice=input('輸入第'+str(4-count)+'個樂透數字:') 
            if choice.isdecimal():
                if int(choice)<=10 and int(choice)>=1:
                    data=int(choice) 
                    player_choice.append(data) 
                    count=count-1
                else:
                    print("此數字不在設定的分數範圍內")
            else:
                print('剛剛輸入的第'+str(count)+'個值並非正整數，請重新輸入')
        except ValueError:
            print("請輸入對的格式")
    while True:
        special_choice = input("請輸入特別獎數字")
        if special_choice.isdecimal():
            if int(special_choice)<=10 and int(special_choice)>=1:
                break
            else:
                print("此數字不在設定的分數範圍內")
        else:
            print('剛剛輸入的數字並非正整數，請重新輸入')
    print("歸檔中...")
    time.sleep(1)
    list1=r.sample(range(1,11), 4) #隨機從1~10選4個數字
    special=list1.pop() #從4個數字裡隨機選取一個數字做為特別獎
    list1.sort()
    print("抽取號碼中...")
    time.sleep(2)
    print("中獎號碼為:", end="")
    for i in range(0,3):
        print(str(list1[i]), end=", ")
    print("特別獎:"+str(special))
    print("玩家樂透數字:", end="")
    for i in range(0,3):
        print(str(player_choice[i]), end=", ")
    print("玩家特別獎數字: ",str(special_choice))
    score=[]
    for i in player_choice:
        for j in list1:
            if int(i) == int(j):
                score.append(1)
            elif int(i) != int(j):
                score.append(0)
    if int(special_choice) == int(special):
        score.append(3)
    else:
        score.append(0)
    accumulated_points=sum(score)
    print("你的積分為:",accumulated_points)
#終極密碼 
def code():
    X=r.randint(1,1001)
    print("請輸入1~1000中的任一整數")
    ans=0
    a=1
    b=1000
    while int(ans)!=X:
        ans=input("")
        if ans.isnumeric():
            if a<=int(ans) and b>=int(ans):
                if int(ans)<X:
                    a=int(ans)+1
                    print("比"+str(ans)+"再大唷嘿嘿嘿")
                    print("請輸入"+str(a)+"到"+str(b)+"的整數")
                elif X<int(ans):
                    b=int(ans)-1
                    print("比"+str(ans)+"還小呵呵呵")
                    print("請輸入"+str(a)+"到"+str(b)+"的整數")
                elif X ==int(ans):
                    print("哇，中了耶")
            else:
                print("請注意範圍")
                print("請輸入"+str(a)+"到"+str(b)+"的整數")
        else:
            print("請輸入整數")
            print("請輸入"+str(a)+"到"+str(b)+"的整數")
            ans=0   
#幾A幾B
def gambling():
    Answer=[]
    list=[0,1,2,3,4,5,6,7,8,9]
    r.shuffle(list)
    for i in range(4):
        Answer.append(list[i])          
    Answers=str(Answer[0])+str(Answer[1])+str(Answer[2])+str(Answer[3])
    guess=""
    A=[]
    B=[]
    AA=[]
    xx=[]
    x=[]
    while guess!=Answers:
        guess=input("請輸入四個不重複的數字(0~9)/放棄")
        for i in range(len(guess)):
            x.append(guess[i])
        if guess.isnumeric():
            if len(guess)!=4:
                print("猜的數字要有四個")
                x=[]
                AA=[]
                A=[]
                B=[]
                xx=[]
            if len(guess)==4:
                if x[1]!=x[2] and x[1]!=x[3] and x[1]!=x[0] and x[2]!=x[3] and x[2]!=x[0] and x[3]!=x[0]:
                    if guess==Answers:
                        print("答對了你個小鬼靈精")
                        print("答案就是",str(Answers))
                    else:
                        for i in range(4):
                            if int(guess[i])==Answer[i]:
                                A.append(1)
                            if int(guess[i])!=Answer[i]:
                                A.append(0)
                        for j in range(4):
                            if A[j]==1:
                                x[j]="無"
                        for g in range(4):
                            if str(x[g]).isnumeric():
                                xx.append(x[g])
                        for k in range(4):
                            if A[k]==0:
                                AA.append(int(Answer[k]))
                        for l in range(len(xx)):
                            if int(xx[l]) in AA:
                                B.append(1)
                        print(str(sum(A))+"A"+str(sum(B))+"B")             
                    AA=[]
                    A=[]
                    B=[]
                    xx=[]
                    x=[]
                else:
                    print("不要輸入重複的數字拉吼唷")
                    x=[]
                    AA=[]
                    A=[]
                    B=[]
                    xx=[]
        if not guess.isnumeric():
            if guess=="放棄":
                print("唉真不中用啊年輕人，too young too simple!")
                print("答案就是",str(Answers),"很難理解嗎?")
                break
            else:
                print("請用數字猜")
                x=[]
                AA=[]
                A=[]
                B=[]
                xx=[]          
            
#撲克牌比大小    
def poker():
    flower = ["♠", "♥", "♣", "♦"]
    number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    pokers = []
    n=1
    for i in flower:
        for j in number:
            pokers.append((n, (i+j)))
            n = n + 1
    print("洗牌中......")
    r.shuffle(pokers)
    def shaf(x):
        for i in x:
            pokers.remove(i)
        return pokers
    def pai(y):
        for i in y:
            print(i[1], ',', end = " ")
    time.sleep(1)
    print("洗牌完成")
    time.sleep(1)
    
    #先發牌給玩家
    player = r.sample(pokers, 3)
    pokers = shaf(player)   
    print("為玩家發牌中......\n")
    player.sort()
    time.sleep(1)
    print("第一回合")
    print("玩家的牌：")
    pai(player)
    print("\n")
    
    #讓玩家從三張手牌決定要選擇出哪一張牌
    while True:        
        draw1 = input("請選擇要出哪一張牌(1/2/3):")           
        try:
            if draw1 == "1":
                player_draw1 = player.pop(0)
                break
            elif draw1 == "2":
                player_draw1 = player.pop(1)
                break
            elif draw1 == "3":
                player_draw1 = player.pop(2)
                break
        except:
              continue         
    computer1 = r.sample(pokers, 1) 
    pokers=shaf(computer1)   
    print("電腦出牌中......\n")
    computer1.sort()
    time.sleep(1)
    print("電腦出的牌：")
    pai(computer1)
    print("\n")
    print("玩家出的牌: ")
    print(player_draw1[1])
    print("\n")
    #電腦與玩家的牌比大小(做不出來，周末再說)(有跟沒有比較沒有影響)

    #讓玩家從剩下的兩張手牌決要出哪一張牌
    print("第二回合")
    print("玩家剩的牌：")
    pai(player)
    print("\n")
    while True:
        try:
            draw2 = input("請選擇要出哪一張牌(1/2):")
            if draw2 == "1":
                player_draw2 = player.pop(0)
                break
            elif draw2 == "2":
                player_draw2 = player.pop(1)
                break
        except:
             continue
    computer2 = r.sample(pokers, 1) 
    pokers=shaf(computer2)   
    print("電腦出牌中......\n")
    computer2.sort()
    time.sleep(1)
    print("電腦出的牌：")
    pai(computer2)
    print("\n")
    print("玩家出的牌: ")
    print(player_draw2[1])
    print("\n")
    
    #玩家丟出剩下的一張牌
    print("第三回合")
    print("玩家剩的牌：")
    pai(player)
    print("\n")
    while True:
        try:
            draw3 = input("你要丟出你剩下的最後一張牌嗎?(yes/no):")
            if draw3 == "yes":
                player_draw3 = player.pop(0)
                break
            elif draw3 == "no":
                player_draw3 = player.pop(0)
                print("嘻嘻,都剩一張牌還不敢出啊?膽小鬼")
                break
        except:
            continue
    computer3 = r.sample(pokers, 1) 
    pokers=shaf(computer3)   
    print("電腦出牌中......\n")
    computer3.sort()
    time.sleep(1)
    print("電腦出的牌：")
    pai(computer3)
    print("\n")
    print("玩家出的牌: ")
    print(player_draw3[1])
    print("\n")
    win=[]
    lose=[]
    #將花色數字化
    if player_draw1[1][0]=="♠":
         player1_suit=4
    if player_draw1[1][0]=="♥":
        player1_suit=3
    if player_draw1[1][0]=="♦":
        player1_suit=2
    if player_draw1[1][0]=="♣":
        player1_suit=1
        
    if player_draw2[1][0]=="♠":
         player2_suit=4
    if player_draw2[1][0]=="♥":
        player2_suit=3
    if player_draw2[1][0]=="♦":
        player2_suit=2
    if player_draw2[1][0]=="♣":
        player2_suit=1
        
    if player_draw3[1][0]=="♠":
         player3_suit=4            
    if player_draw3[1][0]=="♥":
        player3_suit=3
    if player_draw3[1][0]=="♦":
        player3_suit=2
    if player_draw3[1][0]=="♣":
        player3_suit=1
        
    if computer1[0][1][0]=="♠":
        computer1_suit=4
    if computer1[0][1][0]=="♥":
        computer1_suit=3
    if computer1[0][1][0]=="♦":
        computer1_suit=2
    if computer1[0][1][0]=="♣":
        computer1_suit=1
        
    if computer2[0][1][0]=="♠":
        computer2_suit=4
    if computer2[0][1][0]=="♥":
        computer2_suit=3
    if computer2[0][1][0]=="♦":
        computer2_suit=2
    if computer2[0][1][0]=="♣":
        computer2_suit=1
        
    if computer3[0][1][0]=="♠":
        computer3_suit=4
    if computer3[0][1][0]=="♥":
        computer3_suit=3
    if computer3[0][1][0]=="♦":
        computer3_suit=2
    if computer3[0][1][0]=="♣":
        computer3_suit=1
    #將AJQK數字化
    if computer1[0][1][1].isnumeric():
        if len(computer1[0][1])==3:
            computer1v=10
        else:
            computer1v=int(computer1[0][1][1])
    if computer2[0][1][1].isnumeric():
        if len(computer2[0][1])==3:
            computer2v=10
        else:
            computer2v=int(computer2[0][1][1])
    if computer3[0][1][1].isnumeric():
        if len(computer3[0][1])==3:
            computer3v=10
        else:
            computer3v=int(computer3[0][1][1])
    if player_draw1[1][1].isnumeric():
        if len(player_draw1[1])==3:
            player_draw1v=10
        else:
            player_draw1v=int(player_draw1[1][1])
    if player_draw2[1][1].isnumeric():
        if len(player_draw2[1])==3:
            player_draw2v=10
        else:
            player_draw2v=int(player_draw2[1][1])
    if player_draw3[1][1].isnumeric():
        if len(player_draw3[1])==3:
            player_draw3v=10
        else:
            player_draw3v=int(player_draw3[1][1])
    
   
    if computer1[0][1][1]=="A":
        computer1v=14
    if computer1[0][1][1]=="J":
        computer1v=11
    if computer1[0][1][1]=="Q":
        computer1v=12
    if computer1[0][1][1]=="K":
        computer1v=13
        
    if computer2[0][1][1]=="A":
        computer2v=14
    if computer2[0][1][1]=="J":
        computer2v=11
    if computer2[0][1][1]=="Q":
        computer2v=12
    if computer2[0][1][1]=="K":
        computer2v=13
        
    if computer3[0][1][1]=="A":
        computer3v=14
    if computer3[0][1][1]=="J":
        computer3v=11
    if computer3[0][1][1]=="Q":
        computer3v=12
    if computer3[0][1][1]=="K":
        computer3v=13
    
    if player_draw1[1][1]=="A":
        player_draw1v=14
    if player_draw1[1][1]=="J":
        player_draw1v=11
    if player_draw1[1][1]=="Q":
        player_draw1v=12
    if player_draw1[1][1]=="K":
        player_draw1v=13
    
    if player_draw2[1][1]=="A":
        player_draw2v=14
    if player_draw2[1][1]=="J":
        player_draw2v=11
    if player_draw2[1][1]=="Q":
        player_draw2v=12
    if player_draw2[1][1]=="K":
        player_draw2v=13
        
    if player_draw3[1][1]=="A":
        player_draw3v=14
    if player_draw3[1][1]=="J":
        player_draw3v=11
    if player_draw3[1][1]=="Q":
        player_draw3v=12
    if player_draw3[1][1]=="K":
        player_draw3v=13     
        
    if computer1v<player_draw1v:
        win.append(1)
    if computer1v>player_draw1v:
        lose.append(1)
    if computer1v==player_draw1v:
        if  player1_suit>computer1_suit:
            win.append(1)
        else:
            lose.append(1)
            
    if computer2v<player_draw2v:
        win.append(1)
    if computer2v>player_draw2v:
        lose.append(1)
    if computer2v==player_draw2v:
        if  player2_suit>computer2_suit:
            win.append(1)
        else:
            lose.append(1)
    
    if computer3v<player_draw3v:
        win.append(1)
    if computer3v>player_draw3v:
        lose.append(1)
    if computer3v==player_draw3v:
        if  player3_suit>computer3_suit:
            win.append(1)
        else:
            lose.append(1)
    print(str(sum(win))+"勝"+str(sum(lose))+"敗")


# In[ ]:


while True:
    game_start=input("開始遊戲/退出遊戲(請填(yes/no)): ")
    if  game_start == "yes":
        print("進入遊戲菜單")
    elif game_start == "no":
        print("離開遊戲")
        break
    else:
        print("無此選項")
        continue
    while True:
        print("請選擇遊戲(樂透/終極/幾A幾B/撲克牌比大小)\n")
        option=input("(1/2/3/4/quit)")
        if option == "1":  
            lottery()
        elif option == "2": 
            code()
        elif option == "3":  
            gambling()
        elif option == "4":
            poker()
        elif option == "quit":
            print("回到初始選單")
            break
        else:
            print("查無此遊戲")


# In[ ]:




