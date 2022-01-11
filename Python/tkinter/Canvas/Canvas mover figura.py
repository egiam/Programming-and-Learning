
#Ejercicio
import tkinter as tk
import random

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=900, height=500, background="black")
        self.canvas1.grid(column=0, row=0)
        for x in range(103):
            x1=random.randint(1,900)
            y1=random.randint(1,500)
            z=random.randint(1,7)
            if z==1:
                self.cuadrado=self.canvas1.create_rectangle(x1, y1, x1+20, y1+20, fill="green", outline="green", tags="movil")
            elif z==2:
                self.cuadrado=self.canvas1.create_rectangle(x1, y1, x1+20, y1+20, fill="red", outline="red", tags="movil")
            elif z==3:
                self.cuadrado=self.canvas1.create_rectangle(x1, y1, x1+20, y1+20, fill="blue", outline="blue", tags="movil")
            elif z==4:
                self.cuadrado=self.canvas1.create_rectangle(x1, y1, x1+20, y1+20, fill="pink", outline="pink", tags="movil")
            elif z==5:
                self.cuadrado=self.canvas1.create_rectangle(x1, y1, x1+20, y1+20, fill="orange", outline="orange", tags="movil")
            elif z==6:
                self.cuadrado=self.canvas1.create_rectangle(x1, y1, x1+20, y1+20, fill="white", outline="white", tags="movil")
            elif z==7:
                self.cuadrado=self.canvas1.create_rectangle(x1, y1, x1+20, y1+20, fill="yellow", outline="yellow", tags="movil")
        self.canvas1.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
        self.canvas1.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.carta_seleccionada = None
        self.ventana1.mainloop()

    def presion_boton(self, evento):
        carta = self.canvas1.find_withtag(tk.CURRENT)
        self.carta_seleccionada = (carta, evento.x, evento.y)

    def mover(self, evento):
        x, y = evento.x, evento.y
        carta, x1, y1 = self.carta_seleccionada
        self.canvas1.move(carta, x - x1, y - y1)
        self.carta_seleccionada = (carta, x, y)

aplicacion1=Aplicacion()

#Ejemplo
"""
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=900, height=500, background="black")
        self.canvas1.grid(column=0, row=0)
        archi1=tk.PhotoImage(file="carta1.png")
        self.canvas1.create_image(30, 100, image=archi1, anchor="nw", tags="movil")
        archi2=tk.PhotoImage(file="carta2.png")
        self.canvas1.create_image(400, 100, image=archi2, anchor="nw", tags="movil")
        self.canvas1.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
        self.canvas1.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.carta_seleccionada = None
        self.ventana1.mainloop()

    def presion_boton(self, evento):
        carta = self.canvas1.find_withtag(tk.CURRENT)
        self.carta_seleccionada = (carta, evento.x, evento.y)

    def mover(self, evento):
        x, y = evento.x, evento.y
        carta, x1, y1 = self.carta_seleccionada
        self.canvas1.move(carta, x - x1, y - y1)
        self.carta_seleccionada = (carta, x, y)

aplicacion1=Aplicacion()
"""
