from tkinter import ttk
import tkinter
from tkinter.messagebox import showinfo

class MainFrame(ttk.Frame):
    def __init__(self,contenedor):
        super().__init__(contenedor)
        obsiones = {'padx':5,'pady':5}
        
        #label
        self.lb:object = ttk.Label(self,text='TK').pack(**obsiones)
        #btn
        self.btn:object = ttk.Button(self,text='click!',command=self.btn_click).pack(**obsiones)
        #ests pack es de MainFrame
        self.pack(**obsiones)
        
    def btn_click(self):
        showinfo(title='info',message='ok!')

class Aplicacion(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('aplicacion poo')
        self.geometry('600x300+600+300')
    
if __name__ == '__main__':
    app:object = Aplicacion()
    frame:object = MainFrame(app)
    app.mainloop()
        
        