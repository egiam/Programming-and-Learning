

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to my app")

selected = IntVar()

rad1 = Radiobutton(window,text='first', value=1, variable=selected)

rad2 = Radiobutton(window,text='second', value=2, variable=selected)

def clicked():

    print(selected.get())

btn = Button(window, text="Click Me", command=clicked)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

window.mainloop()



from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

selected = IntVar()

rad1 = Radiobutton(window,text='First', value=1, variable=selected)

rad2 = Radiobutton(window,text='Second', value=2, variable=selected)

rad3 = Radiobutton(window,text='Third', value=3, variable=selected)

def clicked():

   print(selected.get())

btn = Button(window, text="Click Me", command=clicked)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)

btn.grid(column=3, row=0)

window.mainloop()



from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

chk_state = BooleanVar()

chk_state.set(True) #set check state

chk = Checkbutton(window, text='Choose', var=chk_state)

chk.grid(column=0, row=0)

window.mainloop()


import tkinter as tk
from tkinter import ttk

class Fruta:

    def __init__(self):
        self.ventana=tk.Tk()
        self.label1=ttk.Label(text="eliga fruta")
        self.label1.grid(column=0, row=0)
        self.fruta=tk.StringVar()
        frutas=("Pera",)
        self.combobox2=ttk.Combobox(self.ventana,width=15,textvariable=self.fruta,values=frutas)
        #self.combobox2.current(0)
        self.combobox2.grid(column=0, row=1)
        self.boton=tk.Button(self.ventana, text='Listo', command=self.Mostrar)
        self.boton.grid(column=0, row=2)
        self.ventana.mainloop()

    def Mostrar(self):
        self.ventana.title(self.combobox2.get())



aplicacion2=Fruta()


#ejercicio1
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(text="Ingrese nombre")
        self.label1.grid(column=0, row=0)
        self.nombre=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=40, textvariable=self.nombre)
        self.entry1.grid(column=0, row=1)
        self.label2=ttk.Label(text="Seleccione país")
        self.label2.grid(column=0, row=2)
        self.pais=tk.StringVar()
        paises=("Argentina","Chile","Bolivia","Paraguay","Brasil","Uruguay")
        self.combobox1=ttk.Combobox(self.ventana1,
                                    width=10,
                                    textvariable=self.pais,
                                    values=paises,
                                    state='readonly')
        #self.combobox1.current(0)
        self.combobox1.grid(column=0, row=3)
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.mostrardatos)
        self.boton1.grid(column=0, row=4)
        self.ventana1.mainloop()

    def mostrardatos(self):
        self.ventana1.title("Nombre:"+self.nombre.get()+" Pais:"+self.combobox1.get())

aplicacion1=Aplicacion()




import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.label=ttk.Label(text="Coloque el nombre y la nacionalidad de la persona.")
        self.label.grid(column=0, row=0)
        self.dato=tk.StringVar()
        self.entry=ttk.Entry(self.ventana1, width=30, textvariable=self.dato)
        self.entry.grid(column=0, row=1)
        self.opcion=tk.StringVar()
        paises=("Argentina","Brasil",'Bolivia','Chile','Colombia','Canada','Ecuador','Estados Unidos','Haiti','Honduras','Mexico','Nicaragua','Paraguay','Panama','Peru','Uruguay','Venezuela')
        self.combobox=ttk.Combobox(self.ventana1,
                                width=10,
                                textvariable=self.opcion,
                                values=paises,
                                state='readonly')
        self.combobox.current(0)
        self.combobox.grid(column=0, row=2)
        self.boton=tk.Button(self.ventana1, text="Listo", command=self.Mostrar)
        self.boton.grid(column=0, row=3)
        self.label1=ttk.Label(text="")
        self.label1.grid(column=0, row=4)
        self.ventana1.mainloop()

    def Mostrar(self):
        mostrar=''
        mostrar+=self.dato.get()+'\n'
        mostrar+='Nacionalidad '+self.opcion.get()
        self.label1.config(text=mostrar)


aplicacion1=Aplicacion()

#Ejemplo1
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(self.ventana1, text="Seleccione un día de la semana")
        self.label1.grid(column=0, row=0)
        self.opcion=tk.StringVar()
        diassemana=("lunes","martes","miércoles","jueves","viernes","sábado","domingo")
        self.combobox1=ttk.Combobox(self.ventana1,
                                  width=10,
                                  textvariable=self.opcion,
                                  values=diassemana)
        self.combobox1.current(0)
        self.combobox1.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=2)
        self.label2=ttk.Label(self.ventana1, text="Día seleccionado:")
        self.label2.grid(column=0, row=3)
        self.ventana1.mainloop()

    def recuperar(self):
        self.label2.configure(text=self.opcion.get())

aplicacion1=Aplicacion()
