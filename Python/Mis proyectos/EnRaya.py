
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random
import sys

class Aplicacion:

    def __init__(self):
        self.ventana=tk.Tk()
        mb.showinfo("Programa","Este programa es una simulacion de un tres en raya")
        self.Ganadas=ttk.Label(self.ventana, text='Partidas Ganadas: ')
        self.Ganadas.grid(column=0, row=0)
        self.wins=0
        self.Rayas()
        self.botones()
        self.botones1()
        self.ventana.mainloop()

    def Rayas(self):
        self.label1=ttk.Label(self.ventana, text='*')
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.label2=ttk.Label(self.ventana, text='*')
        self.label2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.ventana, text='*')
        self.label3.grid(column=2, row=1, padx=4, pady=4)
        self.label4=ttk.Label(self.ventana, text='*')
        self.label4.grid(column=0, row=2, padx=4, pady=4)
        self.label5=ttk.Label(self.ventana, text='*')
        self.label5.grid(column=1, row=2, padx=4, pady=4)
        self.label6=ttk.Label(self.ventana, text='*')
        self.label6.grid(column=2, row=2, padx=4, pady=4)
        self.label7=ttk.Label(self.ventana, text='*')
        self.label7.grid(column=0, row=3, padx=4, pady=4)
        self.label8=ttk.Label(self.ventana, text='*')
        self.label8.grid(column=1, row=3, padx=4, pady=4)
        self.label9=ttk.Label(self.ventana, text='*')
        self.label9.grid(column=2, row=3, padx=4, pady=4)

    def Ganar(self):
        v1=str(self.label1)
        v2=str(self.label2)
        v3=str(self.label3)
        v4=str(self.label4)
        v5=str(self.label5)
        v6=str(self.label6)
        v7=str(self.label7)
        v8=str(self.label8)
        v9=str(self.label9)
        if self.label1==self.label2 and self.label2==vself.label3 or self.label1==self.label5 and self.label5==self.label9:
            mb.showinfo("Ganador",f"Gano el equipo de los {v1}")

    def botones(self):
        self.labelframe1=ttk.LabelFrame(self.ventana, text="Eleccion de X")
        self.labelframe1.grid(column=0, row=4, padx=5, pady=10)
        self.one=0
        self.two=0
        self.three=0
        self.four=0
        self.five=0
        self.six=0
        self.seven=0
        self.eight=0
        self.nine=0
        self.boton1=ttk.Button(self.labelframe1, text="1", command=self.uno)
        self.boton1.grid(column=0, row=0)
        self.boton2=ttk.Button(self.labelframe1, text="2", command=self.dos)
        self.boton2.grid(column=1, row=0)
        self.boton3=ttk.Button(self.labelframe1, text="3", command=self.tres)
        self.boton3.grid(column=2, row=0)
        self.boton4=ttk.Button(self.labelframe1, text="4", command=self.cuatro)
        self.boton4.grid(column=0, row=1)
        self.boton5=ttk.Button(self.labelframe1, text="5", command=self.cinco)
        self.boton5.grid(column=1, row=1)
        self.boton6=ttk.Button(self.labelframe1, text="6", command=self.seis)
        self.boton6.grid(column=2, row=1)
        self.boton7=ttk.Button(self.labelframe1, text="7", command=self.siete)
        self.boton7.grid(column=0, row=2)
        self.boton8=ttk.Button(self.labelframe1, text="8", command=self.ocho)
        self.boton8.grid(column=1, row=2)
        self.boton9=ttk.Button(self.labelframe1, text="9", command=self.nueve)
        self.boton9.grid(column=2, row=2)

    def pintar_X(self,v1):
        if v1==1 and self.one==0:
            self.label1.config(text="X")
            self.one=1
            self.Ganar()
        elif v1==2 and self.two==0:
            self.label2.config(text="X")
            self.two=1
            self.Ganar()
        elif v1==3 and self.three==0:
            self.label3.config(text="X")
            self.three=1
            self.Ganar()
        elif v1==4 and self.four==0:
            self.label4.config(text="X")
            self.four=1
            self.Ganar()
        elif v1==5 and self.five==0:
            self.label5.config(text="X")
            self.five=1
            self.Ganar()
        elif v1==6 and self.six==0:
            self.label6.config(text="X")
            self.six=1
            self.Ganar()
        elif v1==7 and self.seven==0:
            self.label7.config(text="X")
            self.seven=1
            self.Ganar()
        elif v1==8 and self.eight==0:
            self.label8.config(text="X")
            self.eight=1
            self.Ganar()
        elif v1==9 and self.nine==0:
            self.label9.config(text="X")
            self.nine=1
            self.Ganar()

    def uno(self):
        self.pintar_X(1)

    def dos(self):
        self.pintar_X(2)

    def tres(self):
        self.pintar_X(3)

    def cuatro(self):
        self.pintar_X(4)

    def cinco(self):
        self.pintar_X(5)

    def seis(self):
        self.pintar_X(6)

    def siete(self):
        self.pintar_X(7)

    def ocho(self):
        self.pintar_X(8)

    def nueve(self):
        self.pintar_X(9)


    def botones1(self):
        self.labelframe2=ttk.LabelFrame(self.ventana, text="Eleccion de 0")
        self.labelframe2.grid(column=1, row=4, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe2, text="1", command=self.uno1)
        self.boton1.grid(column=0, row=0)
        self.boton2=ttk.Button(self.labelframe2, text="2", command=self.dos1)
        self.boton2.grid(column=1, row=0)
        self.boton3=ttk.Button(self.labelframe2, text="3", command=self.tres1)
        self.boton3.grid(column=2, row=0)
        self.boton4=ttk.Button(self.labelframe2, text="4", command=self.cuatro1)
        self.boton4.grid(column=0, row=1)
        self.boton5=ttk.Button(self.labelframe2, text="5", command=self.cinco1)
        self.boton5.grid(column=1, row=1)
        self.boton6=ttk.Button(self.labelframe2, text="6", command=self.seis1)
        self.boton6.grid(column=2, row=1)
        self.boton7=ttk.Button(self.labelframe2, text="7", command=self.siete1)
        self.boton7.grid(column=0, row=2)
        self.boton8=ttk.Button(self.labelframe2, text="8", command=self.ocho1)
        self.boton8.grid(column=1, row=2)
        self.boton9=ttk.Button(self.labelframe2, text="9", command=self.nueve1)
        self.boton9.grid(column=2, row=2)

    def pintar_O(self,v1):
        if v1==1 and self.one==0:
            self.label1.config(text="0")
            self.one=1
            self.Ganar()
        elif v1==2 and self.two==0:
            self.label2.config(text="0")
            self.two=1
            self.Ganar()
        elif v1==3 and self.three==0:
            self.label3.config(text="0")
            self.three=1
            self.Ganar()
        elif v1==4 and self.four==0:
            self.label4.config(text="0")
            self.four=1
            self.Ganar()
        elif v1==5 and self.five==0:
            self.label5.config(text="0")
            self.five=1
            self.Ganar()
        elif v1==6 and self.six==0:
            self.label6.config(text="0")
            self.six=1
            self.Ganar()
        elif v1==7 and self.seven==0:
            self.label7.config(text="0")
            self.seven=1
            self.Ganar()
        elif v1==8 and self.eight==0:
            self.label8.config(text="0")
            self.eight=1
            self.Ganar()
        elif v1==9 and self.nine==0:
            self.label9.config(text="0")
            self.nine=1
            self.Ganar()

    def uno1(self):
        self.pintar_O(1)

    def dos1(self):
        self.pintar_O(2)

    def tres1(self):
        self.pintar_O(3)

    def cuatro1(self):
        self.pintar_O(4)

    def cinco1(self):
        self.pintar_O(5)

    def seis1(self):
        self.pintar_O(6)

    def siete1(self):
       self.pintar_O(7)

    def ocho1(self):
        self.pintar_O(8)

    def nueve1(self):
        self.pintar_O(9)





aplicacion1=Aplicacion()
