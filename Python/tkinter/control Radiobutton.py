
#ejercicio1
import tkinter as tk

class Aplicacion02:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.label=tk.Label(text="Coloque el color de la pagina al que quiere cambiar")
        self.label.grid(column=0, row=0)
        self.radio1=tk.Radiobutton(self.ventana1, text="Rojo", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.ventana1, text="Azul", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=2)
        self.radio3=tk.Radiobutton(self.ventana1, text="Verde", variable=self.seleccion, value=3)
        self.radio3.grid(column=0, row=3)
        self.boton=tk.Button(self.ventana1, text='Cambiar', command=self.Cambiar)
        self.boton.grid(column=0, row=4)
        self.ventana1.mainloop()

    def Cambiar(self):
        if self.seleccion.get()==1:
            self.ventana1.configure(bg="red")
        elif self.seleccion.get()==2:
            self.ventana1.configure(bg="blue")
        elif self.seleccion.get()==3:
            self.ventana1.configure(bg="green")



aplicacion2=Aplicacion02()

#Ejemplo1
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(text="Ingrese primer valor:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(text="Ingrese segundo valor:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.seleccion=tk.IntVar()
        self.radio1=tk.Radiobutton(self.ventana1,text="Sumar", variable=self.seleccion, value=1)
        self.radio1.grid(column=1, row=2)
        self.radio2=tk.Radiobutton(self.ventana1,text="Restar", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=3)
        self.boton1=tk.Button(self.ventana1, text="Operar", command=self.operar)
        self.boton1.grid(column=1, row=4)
        self.label3=tk.Label(text="resultado")
        self.label3.grid(column=1, row=5)
        self.ventana1.mainloop()

    def operar(self):
        if self.seleccion.get()==1:
            suma=int(self.dato1.get())+int(self.dato2.get())
            self.label3.configure(text=suma)
        if self.seleccion.get()==2:
            resta=int(self.dato1.get())-int(self.dato2.get())
            self.label3.configure(text=resta)

aplicacion1=Aplicacion()

#Ejemplo2
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio1=tk.Radiobutton(self.ventana1,text="Varon", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1,text="Mujer", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Mostrar seleccionado", command=self.mostrarseleccionado)
        self.boton1.grid(column=0, row=2)
        self.label1=tk.Label(text="opcion seleccionada")
        self.label1.grid(column=0, row=3)
        self.ventana1.mainloop()

    def mostrarseleccionado(self):
        if self.seleccion.get()==1:
            self.label1.configure(text="opcion seleccionada=Varon")
        if self.seleccion.get()==2:
            self.label1.configure(text="opcion seleccionada=Mujer")

aplicacion1=Aplicacion()
