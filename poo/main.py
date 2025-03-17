import tkinter
from tkinter import ttk
from enum import Enum
from tkinter.messagebox import showinfo

class Principal(tkinter.Tk):
    def __init__(self):
        super().__init__()
        #config. de ventana
        self.title('poo tkinter')
        self.geometry('600x300+600+300')
        
        #lb
        self.lb:object = ttk.Label(self, text='obten un saludo de tk',borderwidth=2).pack()
        #btn
        self.btn:object = ttk.Button(self,text='click',command=self.click_btn).pack()
    
    def click_btn(self):
        showinfo(title='info.', message='hola')
        
if __name__ == '__main__':
    app:object = Principal()
    app.mainloop()