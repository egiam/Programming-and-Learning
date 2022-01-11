
#ejercicio 2
import tkinter as tk

class Aplicacion03:

    usuarios1=["abc123","abc222"]
    usuarios2=["Juan","Raul"]

    def __init__(self):
        self.ventana1=tk.Tk()
        self.dato1=tk.StringVar()
        self.dato2=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=40, textvariable=self.dato1)
        self.entry1.grid(column=1, row=1)
        self.entry2=tk.Entry(self.ventana1, width=40, textvariable=self.dato2, show='*')
        self.entry2.grid(column=2, row=1)
        self.boton=tk.Button(self.ventana1, text="Go", command=self.Verificar)
        self.boton.grid(column=3, row=1)
        self.label=tk.Label(text="hi")
        self.label.grid(column=2, row=2)
        self.ventana1.mainloop()

    def Verificar(self):
        V1=self.dato1.get()
        V2=self.dato2.get()
        if V2 in Aplicacion03.usuarios1 and V1 in Aplicacion03.usuarios2:
            self.label.config(text="correct password")
        else:
            self.label.config(text="Incorrect password or/and username ")



aplicacion3=Aplicacion03()


#ejercicio1/Calculadora1
import tkinter as tk

class Aplicacion02:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.dato1=tk.StringVar()
        self.dato2=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=5, textvariable=self.dato1)
        self.entry1.grid(column=0, row=0)
        self.entry2=tk.Entry(self.ventana1, width=5, textvariable=self.dato2)
        self.entry2.grid(column=1, row=0)
        self.boton1=tk.Button(self.ventana1, text="Sumar", command=self.Suma)
        self.boton1.grid(column=0, row=1)
        self.boton2=tk.Button(self.ventana1, text="restar", command=self.Resta)
        self.boton2.grid(column=1, row=1)
        self.boton3=tk.Button(self.ventana1, text="Multiplicar", command=self.Mult)
        self.boton3.grid(column=0, row=2)
        self.boton4=tk.Button(self.ventana1, text="Dividir", command=self.Div)
        self.boton4.grid(column=1, row=2)
        self.label=tk.Label(text="")
        self.label.grid(column=1, row=3)
        self.ventana1.mainloop()

    def Suma(self):
        V1=int(self.dato1.get())
        V2=int(self.dato2.get())
        suma=V1+V2
        self.label.config(text=suma)

    def Resta(self):
        V1=int(self.dato1.get())
        V2=int(self.dato2.get())
        resta=V1-V2
        self.label.config(text=resta)

    def Mult(self):
        V1=int(self.dato1.get())
        V2=int(self.dato2.get())
        mult=V1*V2
        self.label.config(text=mult)

    def Div(self):
        V1=int(self.dato1.get())
        V2=int(self.dato2.get())
        div=V1/V2
        self.label.config(text=div)



aplicacion2=Aplicacion02()


#Ejemplo2
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(text="Ingrese nombre de usuario:")
        self.label1.grid(column=0, row=0)
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato)
        self.entry1.grid(column=1, row=0)
        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=1)
        self.ventana1.mainloop()

    def ingresar(self):
        self.ventana1.title(self.dato.get())

aplicacion1=Aplicacion()

#Ejemplo1
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(text="Ingrese un número:")
        self.label1.grid(column=0, row=0)
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        self.entry1.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Calcular Cuadrado", command=self.calcularcuadrado)
        self.boton1.grid(column=0, row=2)
        self.label2=tk.Label(text="resultado")
        self.label2.grid(column=0, row=3)
        self.ventana1.mainloop()

    def calcularcuadrado(self):
        valor=int(self.dato.get())
        cuadrado=valor*valor
        self.label2.configure(text=cuadrado)

aplicacion1=Aplicacion()
