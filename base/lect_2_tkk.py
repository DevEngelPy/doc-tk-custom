import tkinter
from tkinter import ttk
from enum import Enum

class VentanaInfo(Enum):
    titulo:str = 'ttk'
    geometria:str = '600x400+600+300'

#att de la ventana    
app:object = tkinter.Tk()
app.title(VentanaInfo.titulo.value)
app.geometry(VentanaInfo.geometria.value)
app.resizable(False, False)

tkinter.Label(app, text='label info.').pack()
ttk.Label(app, text='label info.').pack()

app.mainloop()