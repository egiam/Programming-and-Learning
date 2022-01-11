
#ejercicio
import tkinter as tk
import sys

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        self.dato=tk.StringVar()
        self.dato2=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=8, textvariable=self.dato)
        self.entry1.grid(column=0, row=0)
        self.entry2=tk.Entry(self.ventana1, width=8, textvariable=self.dato2)
        self.entry2.grid(column=1, row=0)
        self.boton=tk.Button(self.ventana1, text='Change Page Size', command=self.Change)
        self.boton.grid(column=2, row=0)
        self.boton=tk.Button(self.ventana1, text='Finished', command=self.Finish)
        self.boton.grid(column=1, row=1)
        self.ventana1.mainloop()

    def Change(self):
        change=''
        change+=self.dato.get()
        change+='x'
        change+=self.dato2.get()
        self.ventana1.geometry(change)

    def Finish(self):
        sys.exit()



aplicacion1=Aplicacion()

#Ejemplo3
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Rojo", command=self.fijarrojo)
        opciones1.add_command(label="Verde", command=self.fijarverde)
        opciones1.add_command(label="Azul", command=self.fijarazul)
        menubar1.add_cascade(label="Colores", menu=opciones1)
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        submenu1=tk.Menu(menubar1)
        submenu1.add_command(label="1024x1024", command=self.tamano1)
        submenu1.add_command(label="1280x1024", command=self.tamano2)
        opciones2.add_cascade(label="Otros tamaños", menu= submenu1)
        menubar1.add_cascade(label="Tamaños", menu=opciones2)
        self.ventana1.mainloop()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

    def tamano1(self):
        self.ventana1.geometry("1024x1024")

    def tamano2(self):
        self.ventana1.geometry("1280x1024")

aplicacion1=Aplicacion()

#Ejemplo2
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Rojo", command=self.fijarrojo, accelerator="Ctrl+R")
        opciones1.add_command(label="Verde", command=self.fijarverde, accelerator="Ctrl+V")
        opciones1.add_separator()
        opciones1.add_command(label="Azul", command=self.fijarazul, accelerator="Ctrl+A")
        self.ventana1.bind_all("<Control-r>", self.cambiar)
        self.ventana1.bind_all("<Control-v>", self.cambiar)
        self.ventana1.bind_all("<Control-a>", self.cambiar)
        menubar1.add_cascade(label="Colores", menu=opciones1)
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaños", menu=opciones2)
        self.ventana1.mainloop()

    def cambiar(self, event):
        if event.keysym=="r":
            self.fijarrojo()
        if event.keysym=="v":
            self.fijarverde()
        if event.keysym=="a":
            self.fijarazul()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

aplicacion1=Aplicacion()

#Ejemplo1
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Rojo", command=self.fijarrojo)
        opciones1.add_command(label="Verde", command=self.fijarverde)
        opciones1.add_command(label="Azul", command=self.fijarazul)
        menubar1.add_cascade(label="Colores", menu=opciones1)
        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaños", menu=opciones2)
        self.ventana1.mainloop()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

aplicacion1=Aplicacion()
