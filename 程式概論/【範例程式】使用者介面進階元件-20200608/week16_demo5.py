#Programming 101
#week16
#demo 5
#Menu


import tkinter
def width():
    win.title('800x200')
    win.geometry('800x200')
def height():
    win.title('500x500')
    win.geometry('500x500')
def back():
    win.title('500x200')
    win.geometry('500x200')
    
win = tkinter.Tk()
win.geometry('500x200')
win.title('500x200')

menu = tkinter.Menu(win)
win["menu"] = menu
filemenu = tkinter.Menu(menu) #建立子功能表

menu.add_cascade(label="視窗調整", menu=filemenu) #建立子功能表下拉選單
filemenu.add_command(label="視窗變寬...", command=width)
filemenu.add_command(label="視窗變高...", command=height)
filemenu.add_separator() #子功能表內分隔線
filemenu.add_command(label="離開", command=win.destroy)

originalmenu = tkinter.Menu(menu, tearoff=0) #建立取消預設線的子功能表

menu.add_cascade(label = "回復500x200視窗", menu=originalmenu)
originalmenu.add_command(label="回到500x200視窗", command=back)

win.mainloop()
