#Programming 101
#week16
#demo 4
#PhotoImage


import tkinter
from tkinter import messagebox
def showMsg():
    i = radio_v.get()
    if i == 0:
        messagebox.showinfo("選取結果","史努比")
    else:
        messagebox.showinfo("選取結果","史派克")
win=tkinter.Tk()
win.title('小狗偏好選擇')
win.geometry('500x700')
label=tkinter.Label(win, text='請選取您比較喜歡的小狗：').pack()

image1 = tkinter.PhotoImage(file ='snoopy1.gif')
image2 = tkinter.PhotoImage(file ='spike1.gif')

radio_v = tkinter.IntVar()
radio_v.set(0)
tkinter.Radiobutton(win, image=image1, variable=radio_v, value=0).pack()
tkinter.Radiobutton(win, image=image2, variable=radio_v, value=1).pack()

tkinter.Button(win, text = "確定", command = showMsg).pack()

win.mainloop()
