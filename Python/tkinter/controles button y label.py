
#ejercicio2
import tkinter as tk

class Aplicacion01:
    def __init__(self):
        self.label1=[]
        self.ventana1=tk.Tk()
        self.ventana1.title('Botones')
        self.label=tk.Label(self.ventana1, text='')
        self.label.grid(column=0, row=0)
        self.boton1=tk.Button(self.ventana1, text=1, command=self.presion1)
        self.boton1.grid(column=0, row=1)
        self.boton2=tk.Button(self.ventana1, text=2, command=self.presion2)
        self.boton2.grid(column=1, row=1)
        self.boton3=tk.Button(self.ventana1, text=3, command=self.presion3)
        self.boton3.grid(column=0, row=2)
        self.boton4=tk.Button(self.ventana1, text=4, command=self.presion4)
        self.boton4.grid(column=1, row=2)
        self.boton5=tk.Button(self.ventana1, text=5, command=self.presion5)
        self.boton5.grid(column=0, row=3)
        self.boton6=tk.Button(self.ventana1, text='-x', command=self.presion6)
        self.boton6.grid(column=1, row=3)
        self.ventana1.mainloop()

    def presion1(self):
        self.label1.append(1)
        self.label.config(text=self.label1)

    def presion2(self):
        self.label1.append(2)
        self.label.config(text=self.label1)

    def presion3(self):
        self.label1.append(3)
        self.label.config(text=self.label1)

    def presion4(self):
        self.label1.append(4)
        self.label.config(text=self.label1)

    def presion5(self):
        self.label1.append(5)
        self.label.config(text=self.label1)

    def presion6(self):
        self.label1.pop()
        self.label.config(text=self.label1)



botones=Aplicacion01()

#ejercicio 1 por pythonya
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba")
        self.boton1=tk.Button(self.ventana1, text="Varón", command=self.presionvaron)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.presionmujer)
        self.boton2.grid(column=1, row=0)
        self.ventana1.mainloop()

    def presionvaron(self):
        self.ventana1.title('Varón')

    def presionmujer(self):
        self.ventana1.title('Mujer')


aplicacion1=Aplicacion()



#ejercicio1/ da error estando exactamente igual
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title('prueba')
        self.boton1=tk.Button(self.ventana1, text="Varón", command=self.presionvaron)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.presionmujer)
        self.boton2.grid(column=1, row=0)
        self.ventana1.mainloop()

    def presionvaron(self):
        self.ventana1.title('Varón')

    def presionmujer(self):
        self.ventana1.title('Mujer')



generos=Aplicacion()


#Ejemplo2
import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba")
        self.label1=tk.Label(self.ventana1, text="Sistema de facturación")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1, text="2018")
        self.label2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Finalizar", command=self.finalizar)
        self.boton1.grid(column=0, row=2)
        self.ventana1.resizable(False, False)
        self.ventana1.mainloop()


    def finalizar(self):
        sys.exit()

aplicacion1=Aplicacion()

#Ejemplo1
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Controles Button y Label")
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()


    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)


aplicacion1=Aplicacion()
