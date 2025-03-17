import tkinter 
from tkinter import ttk

def btn_clicked()->None:
    print('has echo click!')

def btn_clicked_arg(n1,n2)->None:
    print(n1 + n2)
    
app:object = tkinter.Tk()
app.title('enlace de comandos')
app.geometry('600x400+600+300')
app.resizable(False, False)

btn:object = ttk.Button(app)
btn.config(
    text='btn sin arg',
    command=btn_clicked
    )
btn.pack()

btn_arg:object = ttk.Button(app)
btn_arg.config(
    text='btn con arg',
    command=lambda: btn_clicked_arg(1,2)
)
btn_arg.pack()

app.mainloop()
