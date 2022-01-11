import tkinter as tk
from tkinter import ttk

class Fruta:

    def __init__(self):
        self.ventana=tk.Tk
        self.label1=ttk.Label(text="eliga fruta")
        self.label1.grid(column=0, row=0)
        self.fruta=tk.StringVar()
        frutas=("Pera",)
        self.combobox=ttk.Combobox(self.ventana,
                                width=15,
                                textvariable=self.fruta,
                                values=frutas)
        self.combobox.current(0)
        self.combobox.grid(column=0, row=1)
        self.boton=tk.Button(self.ventana, text='Listo', command=self.Mostrar)
        self.boton.grid(column=0, row=2)
        self.ventana.mainloop()

    def Mostrar(self):
        self.ventana.title(self.combobox1.get())
