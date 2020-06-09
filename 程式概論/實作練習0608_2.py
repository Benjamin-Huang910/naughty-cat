#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter

def SayHello():
    count.set(count.get()+1)
    if count.get() % 2 != 0 :
        lab1["text"] = "Hello, Python!"
    else:
        lab1["text"] = str(count.get())
        


win=tkinter.Tk()
btn=tkinter.Button(win, text="Hello按鈕", command=SayHello)  #建立一個Button的元件
lab1=tkinter.Label(win)        #建立一個Label元件
count = tkinter.IntVar()

btn.pack()
lab1.pack()
win.mainloop()


# In[ ]:




