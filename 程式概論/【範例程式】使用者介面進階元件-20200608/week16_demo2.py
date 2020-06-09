#Programming 101
#week16
#demo 2
#Checkbutton




import tkinter
from tkinter import messagebox
def showMsg():
    result = ''
    for i in check_v:
        if check_v[i].get() == True:
            result = result + country[i] + '  '
    messagebox.showinfo('核取結果', '您想去的國家為：'+result)

win=tkinter.Tk()
win.title('想要旅遊國家調查')
win.geometry('300x150')

label=tkinter.Label(win, text='請選取您想要旅遊的國家：').pack()

country ={0:'土耳其', 1:'英國', 2:'日本', 3:'埃及'}
check_v ={}
for i in range(len(country)):
    check_v[i] = tkinter.BooleanVar()
    tkinter.Checkbutton(win, text=country[i], variable=check_v[i]).pack()

tkinter.Button(win, text='確定', command=showMsg).pack()

win.mainloop()

