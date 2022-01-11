
#ejercicio1
import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.label=tk.Label(text='Nombre y Nacionalidad de la persona.')
        self.label.grid(column=0, row=0)
        self.dato=tk.StringVar()
        self.entry=tk.Entry(self.ventana1, width=40, textvariable=self.dato)
        self.entry.grid(column=0, row=1)
        self.scroll = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(self.ventana1, yscrollcommand=self.scroll.set)
        self.listbox1.grid(column=0, row=2)
        self.scroll.configure(command=self.listbox1.yview)
        self.scroll.grid(column=1, row=2, sticky='NS')

        self.listbox1.insert(0,"Argentina")
        self.listbox1.insert(1,"Brasil")
        self.listbox1.insert(2,"Bolivia")
        self.listbox1.insert(3,"Chile")
        self.listbox1.insert(4,"Colombia")
        self.listbox1.insert(5,"Canada")
        self.listbox1.insert(6,"Ecuador")
        self.listbox1.insert(7,"Estados Unidos")
        self.listbox1.insert(8,"Haiti")
        self.listbox1.insert(9,"Honduras")
        self.listbox1.insert(10,"Mexico")
        self.listbox1.insert(11,"Nicaragua")
        self.listbox1.insert(12,"Paraguay")
        self.listbox1.insert(13,"Panama")
        self.listbox1.insert(14,"Peru")
        self.listbox1.insert(15,"Uruguay")
        self.listbox1.insert(16,"Venezuela")
        
        self.boton=tk.Button(self.ventana1, text='Listo', command=self.Mostrar)
        self.boton.grid(column=0, row=3)
        self.label1=tk.Label(text='')
        self.label1.grid(column=0, row=4)
        self.ventana1.mainloop()

    def Mostrar(self):
        if len(self.listbox1.curselection())!=0:
            mostrar=''
            mostrar+=self.dato.get()+'\n'
            mostrar+='De '+self.listbox1.get(self.listbox1.curselection()[0])
            self.label1.config(text=mostrar)



aplicacion1=Aplicacion()

#Ejemplo3
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.scroll1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set)
        self.listbox1.grid(column=0,row=0)
        self.scroll1.configure(command=self.listbox1.yview)
        self.scroll1.grid(column=1, row=0, sticky='NS')
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.listbox1.insert(6,"limon")
        self.listbox1.insert(7,"kiwi")
        self.listbox1.insert(5,"banana")
        self.listbox1.insert(5,"uva")
        self.listbox1.insert(5,"papaya")
        self.listbox1.insert(5,"mandarina")
        self.listbox1.insert(5,"frutilla")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(text="Seleccionado:")
        self.label1.grid(column=0, row=2)
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todas=''
            for posicion in self.listbox1.curselection():
                todas+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todas)

aplicacion1=Aplicacion()

#Ejemplo2
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(text="Seleccionado:")
        self.label1.grid(column=0, row=2)
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todas=''
            for posicion in self.listbox1.curselection():
                todas+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todas)

aplicacion1=Aplicacion()

#Ejemplo1
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(text="Seleccionado:")
        self.label1.grid(column=0, row=2)
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.label1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1=Aplicacion()
