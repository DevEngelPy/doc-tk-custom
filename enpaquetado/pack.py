import tkinter 
from tkinter import ttk

app:object = tkinter.Tk()
app.title('pack')
app.geometry('600x300+600+300')
app.resizable(False, False)

lb1:object = ttk.Label(app,text='label 1', background='red', font='white').pack(
    side=tkinter.TOP,
    expand=False,
    fill=tkinter.X,
    ipady=40,
    anchor=tkinter.W
    )
lb2:object = ttk.Label(app,text='label 2', background='blue', font='white').pack(side=tkinter.BOTTOM, expand=True, fill=tkinter.BOTH,ipadx=80,anchor=tkinter.E)
lb3:object = ttk.Label(app,text='label 3', background='green', font='white').pack(side=tkinter.LEFT, expand=False, fill=tkinter.Y, ipadx=40,ipady=40)

app.mainloop()