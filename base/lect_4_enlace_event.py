import tkinter
from tkinter import ttk

def tecla_presionado(event):
    print('tecla presionada')

app:object = tkinter.Tk()

btn:object = ttk.Button(app, text='guardar')
btn.bind('<Return>', tecla_presionado)
btn.focus()
btn.pack(expand=True)


app.mainloop()