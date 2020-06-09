#Programming 101
#week16
#demo 1
#messagebox



import tkinter
from tkinter import messagebox
def showMsg():
    Ans=messagebox.askquestion('年齡問題','你已滿18歲了嗎？')
    if(Ans=='yes'):
        messagebox.showinfo('恭喜','您已成年！')
    else:
        messagebox.showinfo('很抱歉','您尚未成年喔！')

win = tkinter.Tk()
win.title('年齡判斷程式')
win.geometry('300x100')

btn = tkinter.Button(win,text='跳出對話方塊', command=showMsg)
btn.pack()

win.mainloop()
