
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        self.labelframe=ttk.LabelFrame(self.ventana, text='Calculadora')
        self.labelframe.grid(column=0, row=0, padx=5, pady=10)
        self.IngresoVal()
        self.labelframe1=ttk.LabelFrame(self.ventana, text='Calculadora')
        self.labelframe1.grid(column=0, row=1, padx=5, pady=10)
        self.Calculos()
        self.ventana.mainloop()

    def IngresoVal(self):
        self.valor1=tk.StringVar()
        self.valor2=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe, width=10, textvariable=self.valor1)
        self.entry1.grid(column=0, row=0, padx=4, pady=5)
        self.label1=ttk.Label(self.labelframe, text='')
        self.label1.grid(column=1, row=0, padx=4, pady=5)
        self.entry2=ttk.Entry(self.labelframe, width=10, textvariable=self.valor2)
        self.entry2.grid(column=2, row=0, padx=4, pady=5)
        self.label2=ttk.Label(self.labelframe, text='=')
        self.label2.grid(column=3, row=0, padx=4, pady=5)
        self.label3=ttk.Label(self.labelframe, text='')
        self.label3.grid(column=4, row=0, padx=4, pady=5)

    def Calculos(self):
        self.suma=tk.Button(self.labelframe1, text='+', command=self.Suma)
        self.suma.grid(column=0, row=0)
        self.resta=tk.Button(self.labelframe1, text='-', command=self.Resta)
        self.resta.grid(column=1, row=0)
        self.mult=tk.Button(self.labelframe1, text='x', command=self.Mult)
        self.mult.grid(column=0, row=1)
        self.div=tk.Button(self.labelframe1, text='%', command=self.Div)
        self.div.grid(column=1, row=1)
        self.exp=tk.Button(self.labelframe1, text='^', command=self.Exp)
        self.exp.grid(column=3, row=0)
        self.raiz=tk.Button(self.labelframe1, text='#', command=self.Raiz)
        self.raiz.grid(column=3, row=1)
        self.fin=tk.Button(self.ventana, text='Finished', command=self.Fin)
        self.fin.grid(column=0, row=3, padx=5, pady=10)

    def Suma(self):
        V1=int(self.valor1.get())
        V2=int(self.valor2.get())
        resultado=V1+V2
        self.label1.config(text='+')
        self.label3.config(text=resultado)

    def Resta(self):
        V1=int(self.valor1.get())
        V2=int(self.valor2.get())
        resultado=V1-V2
        self.label1.config(text='-')
        self.label3.config(text=resultado)

    def Mult(self):
        V1=int(self.valor1.get())
        V2=int(self.valor2.get())
        resultado=V1*V2
        self.label1.config(text='x')
        self.label3.config(text=resultado)

    def Div(self):
        V1=int(self.valor1.get())
        V2=int(self.valor2.get())
        resultado=V1/V2
        self.label1.config(text='%')
        self.label3.config(text=resultado)

    def Exp(self):
        V1=int(self.valor1.get())
        V2=int(self.valor2.get())
        resultado=V1**V2
        self.label1.config(text='^')
        self.label3.config(text=resultado)

    def Raiz(self):
        V1=int(self.valor1.get())
        V2=int(self.valor2.get())
        x=0
        while  x**V2<=V1:
            x += 0.000001
        resultado=round(x, 5)
        self.label1.config(text='#')
        self.label3.config(text=resultado)

    def Fin(self):
        respuesta=mb.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta==True:
            sys.exit()



aplicacion1=Aplicacion()
