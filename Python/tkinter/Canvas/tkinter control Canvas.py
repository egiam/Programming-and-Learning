
#Ejercicio
import tkinter as tk
from tkinter import ttk

class App:

    def __init__(self):
        self.ventana=tk.Tk()
        self.entradadatos()
        self.canvas=tk.Canvas(self.ventana, width=600, height=400, background='black')
        self.canvas.grid(column=0, row=1)
        self.ventana.mainloop()

    def entradadatos(self):
        self.lf1=ttk.LabelFrame(self.ventana,text="Partidos políticos")
        self.lf1.grid(column=0, row=0, sticky="w")
        self.label1=ttk.Label(self.lf1, text="Partido A:")
        self.label1.grid(column=0,row=0, padx=5, pady=5)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.lf1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.lf1, text="Partido B:")
        self.label2.grid(column=0,row=1, padx=5, pady=5)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.lf1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.label3=ttk.Label(self.lf1, text="Partido C:")
        self.label3.grid(column=0,row=2, padx=5, pady=5)
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.lf1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5)
        self.boton1=ttk.Button(self.lf1, text="Generar gráfico", command=self.Barra_porcentual)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
        self.entry1.focus()

    def Barra_porcentual(self):
        self.canvas.delete(tk.ALL)
        val1=int(self.dato1.get())
        val2=int(self.dato2.get())
        val3=int(self.dato3.get())
        suma=val1+val2+val3
        largo1=val1/suma*500
        largo2=val2/suma*500
        largo3=val3/suma*500
        porc1=val1/suma*100
        porc2=val2/suma*100
        porc3=val3/suma*100
        self.canvas.create_rectangle(10,200,10+largo1,260,fill="red")
        self.canvas.create_text(50, 220, text="{0:.2f}".format(porc1)+"%", fill="white", font="Arial")
        self.canvas.create_rectangle(10+largo1,200,10+largo1+largo2,260,fill="green")
        self.canvas.create_text(50+largo1, 220, text="{0:.2f}".format(porc2)+"%", fill="white", font="Arial")
        self.canvas.create_rectangle(10+largo1+largo2,200,10+largo1+largo2+largo3,260,fill="blue")
        self.canvas.create_text(50+largo1+largo2, 220, text="{0:.2f}".format(porc3)+"%", fill="white", font="Arial")



aplicacion12=App()

#Ejemplo3
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.entradadatos()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=1)
        self.ventana1.mainloop()

    def entradadatos(self):
        self.lf1=ttk.LabelFrame(self.ventana1,text="Partidos políticos")
        self.lf1.grid(column=0, row=0, sticky="w")
        self.label1=ttk.Label(self.lf1, text="Partido A:")
        self.label1.grid(column=0,row=0, padx=5, pady=5)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.lf1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.lf1, text="Partido B:")
        self.label2.grid(column=0,row=1, padx=5, pady=5)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.lf1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.label3=ttk.Label(self.lf1, text="Partido C:")
        self.label3.grid(column=0,row=2, padx=5, pady=5)
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.lf1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5)
        self.boton1=ttk.Button(self.lf1, text="Generar gráfico", command=self.grafico_tarta)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
        self.entry1.focus()

    def grafico_tarta(self):
        self.canvas1.delete(tk.ALL)
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        valor3=int(self.dato3.get())
        suma=valor1+valor2+valor3
        grados1=valor1/suma*360
        grados2=valor2/suma*360
        grados3=valor3/suma*360
        self.canvas1.create_arc(10,10,400,400,fill="red", start=0, extent=grados1)
        self.canvas1.create_arc(10,10,400,400,fill="blue", start=grados1, extent=grados2)
        self.canvas1.create_arc(10,10,400,400,fill="yellow", start=grados1+grados2, extent=grados3)
        self.canvas1.create_text(500, 50, text="partido A:"+str(valor1), fill="red", font="Arial")
        self.canvas1.create_text(500, 100, text="partido B:"+str(valor2), fill="blue", font="Arial")
        self.canvas1.create_text(500, 150, text="partido C:"+str(valor3), fill="yellow", font="Arial")


aplicacion1=Aplicacion()

#Ejemplo2
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.entradadatos()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=1)
        self.ventana1.mainloop()

    def entradadatos(self):
        self.lf1=ttk.LabelFrame(self.ventana1,text="Partidos políticos")
        self.lf1.grid(column=0, row=0, sticky="w")
        self.label1=ttk.Label(self.lf1, text="Partido A:")
        self.label1.grid(column=0,row=0, padx=5, pady=5)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.lf1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.lf1, text="Partido B:")
        self.label2.grid(column=0,row=1, padx=5, pady=5)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.lf1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.label3=ttk.Label(self.lf1, text="Partido C:")
        self.label3.grid(column=0,row=2, padx=5, pady=5)
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.lf1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5)
        self.boton1=ttk.Button(self.lf1, text="Generar gráfico", command=self.grafico_barra)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
        self.entry1.focus()

    def grafico_barra(self):
        self.canvas1.delete(tk.ALL)
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        valor3=int(self.dato3.get())
        if valor1>valor2 and valor1>valor3:
            mayor=valor1
        else:
            if valor2>valor3:
                mayor=valor2
            else:
                mayor=valor3
        largo1=valor1/mayor*400
        largo2=valor2/mayor*400
        largo3=valor3/mayor*400
        self.canvas1.create_rectangle(10,10,10+largo1,90,fill="red")
        self.canvas1.create_rectangle(10,120,10+largo2,200,fill="blue")
        self.canvas1.create_rectangle(10,230,10+largo3,310,fill="green")
        self.canvas1.create_text(largo1+70, 50, text="partido A", fill="white", font="Arial")
        self.canvas1.create_text(largo2+70, 160, text="partido B", fill="white", font="Arial")
        self.canvas1.create_text(largo3+70, 270, text="partido C", fill="white", font="Arial")


aplicacion1=Aplicacion()

#Ejemplo1
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.create_line(0, 0, 100,50, fill="white")
        self.canvas1.create_rectangle(150,10, 250,110, fill="white")
        self.canvas1.create_oval(300,10,400,150, fill="red")
        self.canvas1.create_arc(420,10,550,110, fill="yellow", start=180, extent=90)
        self.canvas1.create_rectangle(150,210, 250,310, outline="white")
        self.canvas1.create_oval(300,210,400,350, outline="red")
        self.canvas1.create_arc(420,210,550,310, outline="yellow", start=180, extent=90)
        self.ventana1.mainloop()


aplicacion1=Aplicacion()
