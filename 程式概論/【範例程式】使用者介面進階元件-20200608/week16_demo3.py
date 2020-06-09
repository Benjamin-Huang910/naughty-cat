#Programming 101
#week16
#demo 3
#radiobutton


import tkinter
from tkinter import messagebox
def showMsg():
    i=radio_v.get()
    messagebox.showinfo('選取結果', '您最想去的國家為：'+country[i])
win=tkinter.Tk()
win.title('最想要旅遊國家調查')
win.geometry('300x150')

label=tkinter.Label(win, text='請選取您最想要旅遊的國家：').pack()
country={0:'土耳其', 1:'英國', 2:'日本', 3:'埃及'}
radio_v = tkinter.IntVar()
radio_v.set(0)
for i in range(len(country)):
    tkinter.Radiobutton(win,text=country[i],variable=radio_v,value=i).pack()

tkinter.Button(win, text = "確定", command=showMsg).pack()

win.mainloop()


