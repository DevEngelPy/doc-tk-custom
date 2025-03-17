from tkinter import Tk
from enum import Enum



class VentanaInfo(Enum):
    TITULO:str = 'sysmoreno'
    TAMANO:str = '600x400+600+300'
    ICON:str = './static/icons-sys-engel.png'
"""
basico tk
""" 
#crea una nueva ventana
app:object = Tk()
#titulo ventana
app.title(VentanaInfo.TITULO.value)
#medida de la ventana
app.geometry(VentanaInfo.TAMANO.value)
#evita que el usuario modifique el tamaño
app.resizable(False,False)
#tranparencia de la ventana
#app.attributes('-alpha', 0.5)
#icono
app.iconbitmap(VentanaInfo.ICON.value)


#ejecuta y mantiene la ejecucion del prog.
app.mainloop()