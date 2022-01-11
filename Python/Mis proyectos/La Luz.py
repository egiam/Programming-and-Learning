
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys


class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.config(background='black')
        self.labelframe1=ttk.LabelFrame(self.ventana, text='Luz')
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.Luz()
        self.Comandos()
        self.ventana.mainloop()

    def Luz(self):
        self.label=ttk.Label(self.labelframe1, text='Off')
        self.label.grid(column=0, row=0, padx=4, pady=5)
        self.luz='Off'

    def Comandos(self):
        self.boton=ttk.Button(self.ventana, text='Luz', command=self.Cambio)
        self.boton.grid(column=0, row=1, padx=4, pady=5)

    def Cambio(self):
        if self.luz=='Off':
            self.label.config(text='On')
            self.ventana.config(background='yellow')
            self.luz='On'
        elif self.luz=='On':
            self.label.config(text='Off')
            self.ventana.config(background='black')
            self.luz='Off'



aplicacion1=Aplicacion()
