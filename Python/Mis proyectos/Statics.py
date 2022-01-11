
import pandas as pd
import tkinter as tk
from tkinter import ttk

class Estadisticas1:

    def __init__(self):
        self.ventana=tk.Tk()
        self.Nombre()
        self.ventana.mainloop()

    def Nombre(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text='Nombre')
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text='Nombre del personaje: ')
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.Name=tk.StringVar()
        self.nameentry=ttk.Entry(self.labelframe1, width=15, textvariable=self.Name)
        self.nameentry.grid(column=0, row=1, padx=4, pady=4)
        self.labelframe2=ttk.LabelFrame(self.ventana1, text='Edad')
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)
        self.label2=ttk.Label(self.labelframe2, text='Edad del personaje: ')
        self.label2.grid(column=0, row=0, padx=4, pady=4)
        self.Age=tk.StringVar()
        self.ageentry=ttk.Entry(self.labelframe2, width=15, textvariable=self.Age)
        self.nameentry.grid(column=0, row=1, padx=4, pady=4)
        self.ventana1.mainloop()



estadisticas=Estadisticas1()
