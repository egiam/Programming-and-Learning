
#Ejemplo3
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("800x600")
        self.ventana1.resizable(0,0)
        self.boton1=ttk.Button(self.ventana1, text="Confirmar")
        self.boton1.place(x=680, y=550, width=90, height=30)
        self.boton2=ttk.Button(self.ventana1, text="Cancelar")
        self.boton2.place(x=580, y=550, width=90, height=30)
        self.ventana1.mainloop()

aplicacion1=Aplicacion()

#Ejemplo2
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=ttk.Button(self.ventana1, text="Boton 1")
        self.boton1.grid(column=0, row=0)
        self.boton2=ttk.Button(self.ventana1, text="Boton 2")
        self.boton2.grid(column=1, row=0)
        self.boton3=ttk.Button(self.ventana1, text="Boton 3")
        self.boton3.grid(column=2, row=0, rowspan=2, sticky="ns")
        self.boton4=ttk.Button(self.ventana1, text="Boton 4")
        self.boton4.grid(column=0, row=1)
        self.boton5=ttk.Button(self.ventana1, text="Boton 5")
        self.boton5.grid(column=1, row=1)
        self.boton6=ttk.Button(self.ventana1, text="Boton 6")
        self.boton6.grid(column=0, row=2, columnspan=3, sticky="we")
        self.ventana1.mainloop()

aplicacion1=Aplicacion()

#Ejemplo1
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=ttk.Button(self.ventana1, text="Boton 1")
        self.boton1.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton2=ttk.Button(self.ventana1, text="Boton 2")
        self.boton2.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton3=ttk.Button(self.ventana1, text="Boton 3")
        self.boton3.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton4=ttk.Button(self.ventana1, text="Boton 4")
        self.boton4.pack(side=tk.LEFT)
        self.boton5=ttk.Button(self.ventana1, text="Boton 5")
        self.boton5.pack(side=tk.RIGHT)
        self.boton6=ttk.Button(self.ventana1, text="Boton 6")
        self.boton6.pack(side=tk.RIGHT)
        self.boton7=ttk.Button(self.ventana1, text="Boton 7")
        self.boton7.pack(side=tk.RIGHT)
        self.ventana1.mainloop()

aplicacion1=Aplicacion()
