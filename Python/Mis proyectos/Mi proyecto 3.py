
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random
import sys

class Aplicacion:


        #Principal

    def __init__(self):
        self.ventana=tk.Tk()
        self.estadisticas=ttk.LabelFrame(self.ventana, text='Estadisticas:')
        self.estadisticas.grid(column=0, row=0, padx=5, pady=10)
        self.Stadistics()
        self.tiempo=ttk.LabelFrame(self.ventana, text='Tiempo:')
        self.tiempo.grid(column=1, row=0, padx=5, pady=10)
        self.Time()
        self.opciones1=ttk.LabelFrame(self.ventana, text='opciones')
        self.opciones1.grid(column=0, row=1, padx=5, pady=10)
        self.Options1()
        self.opciones2=ttk.LabelFrame(self.ventana, text='opciones')
        self.opciones2.grid(column=1, row=1, padx=5, pady=10)
        self.Options2()
        self.ventana.mainloop()


        #Estadisticas

    def Stadistics(self):
        self.Name=ttk.Label(self.estadisticas, text='Nombre: Raul Guztamante')
        self.Name.grid(column=0, row=0, padx=4, pady=4)
        self.Money=ttk.Label(self.estadisticas, text='Dinero: 50')
        self.Money.grid(column=0, row=1, padx=4, pady=4)
        self.Dinero=50
        self.Peso=ttk.Label(self.estadisticas, text='Peso: 10')
        self.Peso.grid(column=1, row=0, padx=4, pady=4)
        self.peso=10
        self.Fuerza=ttk.Label(self.estadisticas, text='Fuerza: 10')
        self.Fuerza.grid(column=0, row=2, padx=4, pady=4)
        self.fuerza=10
        self.Saber=ttk.Label(self.estadisticas, text='Sabiduria: 5')
        self.Saber.grid(column=1, row=1, padx=4, pady=4)
        self.knowment=5
        self.Amor=ttk.Label(self.estadisticas, text='Amor: 3')
        self.Amor.grid(column=1, row=2, padx=4, pady=4)
        self.Love=3


        #Tiempos

    def Time(self):
        self.Hora=ttk.Label(self.tiempo, text='09:00')
        self.Hora.grid(column=0, row=0, padx=4, pady=4)
        hora='Hora: '
        self.time=9
        hora += str(self.time)
        hora += ":00"
        self.Hora.config(text=hora)
        dia="Dia: "
        dia+=str(1)
        self.dias=1
        self.Dia=ttk.Label(self.tiempo, text=dia)
        self.Dia.grid(column=0, row=1, padx=4, pady=4)
        self.meses=1
        self.Mes=ttk.Label(self.tiempo, text='Mes: 1')
        self.Mes.grid(column=1, row=0, padx=4, pady=4)
        self.years=1
        self.Year=ttk.Label(self.tiempo, text='Año: 1')
        self.Year.grid(column=1, row=1, padx=4, pady=4)
        self.Dias()
        self.Meses()
        self.Years()

    def Dias(self):
        Hs=self.time
        if Hs>=24:
            self.dias+=1
            dia='Dia: '
            dia+=str(self.dias)
            self.Dia.config(text=dia)
            self.time=self.time-24
            hora='Hora: '
            hora+=str(self.time)
            hora+=':00'
            self.Hora.config(text=hora)

    def Meses(self):
        Ms=self.dias
        if Ms>30:
            self.meses+=1
            mes='Mes: '
            mes+=str(self.meses)
            self.Mes.config(text=mes)
            self.dias=self.dias-30
            dia="Dia: "
            dia+=str(self.dias)
            self.Dia.config(text=dia)

    def Years(self):
        Ys=self.meses
        if Ys>12:
            self.years+=1
            Año='Año: '
            Año+=str(self.years)
            self.Year.config(text=Año)
            self.meses=self.meses-12
            Mes="Mes: "
            Mes+=str(self.meses)
            self.Mes.config(text=Mes)


            #Opciones de que hacer desde casa

    def Options1(self):
        self.Trabajar=ttk.Button(self.opciones1, text='Trabajar (Dinero +100/ Tiempo +6hs)', command=self.Work)
        self.Trabajar.grid(column=0, row=0, padx=4, pady=4)
        self.v1=100
        self.Jugar=ttk.Button(self.opciones1, text='Jugar (Dinero -20/ Peso +1/ Tiempo +4hs)', command=self.Play)
        self.Jugar.grid(column=0, row=1, padx=4, pady=4)
        self.Dormir=ttk.Button(self.opciones1, text='Dormir (Tiempo +8hs)', command=self.Sleep)
        self.Dormir.grid(column=0, row=2, padx=4, pady=4)
        self.Internet=ttk.Button(self.opciones1, text='Internet (Peso +1/ Tiempo +4hs/ sabiduria+1)', command=self.WiFi)
        self.Internet.grid(column=1, row=0, padx=4, pady=4)
        self.Comer=ttk.Button(self.opciones1, text='Comer (Peso +1/ Tiempo +1hs/ Dinero -10)', command=self.Eat)
        self.Comer.grid(column=1, row=1, padx=4, pady=4)
        self.Estudiar=ttk.Button(self.opciones1, text='Estudiar (sabiduria +2/ Tiempo +4hs/ Dinero -200)', command=self.Study)
        self.Estudiar.grid(column=1, row=2, padx=4, pady=4)

        #Comandos para subir estadisticas

    def comandos(self):
        if self.time>=24:
            self.Dias()
        elif self.dias>30:
            self.Meses()
        elif self.meses>12:
            self.Years()

    def Cash(self,v1):
        self.Dinero=self.Dinero-v1
        dinero='Dinero: '
        dinero+=str(self.Dinero)
        self.Money.config(text=dinero)

    def Debt(self,v1,v2,v3,v4,v5,v6):
        if v1>0:
            if self.Dinero<=0 or self.Dinero<v1:
                mb.showerror("Cuidado", "Necesita tener dinero antes de gastarlo.")
            else:
                self.Cash(v1)
                self.agregar_time(v2)
                self.Peso1(v3)
                self.Strenght(v4)
                self.Sabiduria(v5)
                self.Lovement(v6)
        elif v1==0:
            self.Cash(v1)
            self.agregar_time(v2)
            self.Peso1(v3)
            self.Strenght(v4)
            self.Sabiduria(v5)
            self.Lovement(v6)

    def agregar_time(self,v2):
        self.time=self.time+v2
        tiempo='Hora: '
        tiempo+=str(self.time)
        tiempo+=':00'
        self.Hora.config(text=tiempo)

    def Peso1(self,v3):
        self.peso=self.peso+v3
        pess='Peso: '
        pess+=str(self.peso)
        self.Peso.config(text=pess)
        if self.peso<-5 and self.peso>-10:
            mb.showinfo("Sube de peso","Sube un poco de peso o moriras de anorexcia")
        elif self.peso<=-10:
            mb.showinfo("Moriste de anorexcia","Has muerto de anorexcia, por favor, la proxima vez sea mas cuidadoso")
            sys.exit()
        if self.peso>80 and self.peso<100:
            mb.showinfo("Baja de peso","Baja un poco de peso o moriras de sobrepeso")
        elif self.peso>=100:
            mb.showinfo("Moriste","Has muerto de un paro cardiaco por el sobrepeso, por favor, la proxima vez sea mas cuidadoso")
            sys.exit()

    def Strenght(self,v4):
        self.fuerza=self.fuerza+v4
        frz="Fuerza: "
        frz+=str(self.fuerza)
        self.Fuerza.config(text=frz)

    def Sabiduria(self,v5):
        self.knowment=self.knowment+v5
        knw="Sabiduria: "
        knw+=str(self.knowment)
        self.Saber.config(text=knw)
        if v5>0:
            self.v1=self.v1+10*v5

    def Cash_Work(self):
        trabajo="Trabajar: (Dinero: +"
        trabajo+=str(self.v1)
        trabajo+="// Tiempo +6hs)"
        self.Trabajar.config(text=trabajo)
        self.Dinero=self.Dinero+self.v1
        dinero='Dinero: '
        dinero+=str(self.Dinero)
        self.Money.config(text=dinero)

    def Lovement(self,v6):
        self.Love=self.Love+v6
        love="Amor: "
        love+=str(self.Love)
        self.Amor.config(text=love)

        #Comandos de las opciones desde casa

    def Work(self):
        self.Cash_Work()
        self.agregar_time(6)
        self.comandos()

    def Play(self):
        self.Debt(20,4,1,0,0,0)
        self.comandos()

    def Sleep(self):
        self.Debt(0,8,0,0,0,0)
        self.comandos()

    def WiFi(self):
        self.Debt(0,4,1,0,1,0)
        self.comandos()

    def Eat(self):
        self.Debt(10,1,1,0,0,0)
        self.comandos()

    def Study(self):
        v1=self.knowment*20
        texto='Estudiar (sabiduria +2/ Tiempo +4hs/ Dinero -'
        texto+=str(v1)
        texto+=')'
        self.Estudiar.config(text=texto)
        self.Debt(v1,4,0,0,2,0)
        self.comandos()


        #Opciones de que hacer fuera de casa

    def Options2(self):
        self.Ejercicio=ttk.Button(self.opciones2, text='Ejercicio (Fuerza +1/ Peso -1/ Tiempo +2hs/ Dinero -20)', command=self.Gym)
        self.Ejercicio.grid(column=0, row=0, padx=4, pady=4)
        self.Tienda=ttk.Button(self.opciones2, text='Tienda (Tiempo +2hs/ Dinero -100)', command=self.Store)
        self.Tienda.grid(column=0, row=1, padx=4, pady=4)
        self.Super=ttk.Button(self.opciones2, text='Super (Tiempo +3hs/ Dinero -150)', command=self.Mall)
        self.Super.grid(column=0, row=2, padx=4, pady=4)
        self.Shopping=ttk.Button(self.opciones2, text='Shopping (Tiempo +4hs/ Dinero -200)', command=self.shopping)
        self.Shopping.grid(column=1, row=0, padx=4, pady=4)
        self.Tinder=ttk.Button(self.opciones2, text='Tinder (Tiempo +3hs/ Dinero -120/ Amor +1)', command=self.Cita)
        self.Tinder.grid(column=1, row=1, padx=4, pady=4)
        self.Loteria=ttk.Button(self.opciones2, text='Loteria (Dinero -10)', command=self.Lottery)
        self.Loteria.grid(column=1, row=2, padx=4, pady=4)

    def Gym(self):
        self.Debt(20,2,-1,1,0,0)
        self.comandos()

    def Store(self):
        self.Debt(100,2,0,0,0,0)
        self.comandos()

    def Mall(self):
        self.Debt(150,3,0,0,0,0)
        self.comandos()

    def shopping(self):
        self.Debt(200,4,0,0,0,0)
        self.comandos()

    def Cita(self):
        self.Debt(120,3,1,0,0,1)
        self.comandos()

    def Lottery(self):
        self.Debt(10,0,0,0,0,0)
        self.comandos()
        self.Numero()

    def Numero(self):
        Xr=random.randint(1,1000000)
        Diez=[3454,23523,23,231,3445,12333,67774,23445,86756,1223,2,123333,454665,456453,12,7,77,777,7777,77777,777777]
        for x in range(len(Diez)):
            if Xr==Diez[x]:
                mb.showinfo("Ganaste","Has ganado 10.000 de dolares en la Loteria")
                self.Dinero=self.Dinero+10001
                self.Dinero=self.Dinero-1
                dinero='Dinero: '
                dinero+=str(self.Dinero)
                self.Money.config(text=dinero)
        Cien=[9,98,987,9876,98765,987654]
        for x in range(len(Cien)):
            if Xr==Cien[x]:
                mb.showinfo("Ganaste","Has ganado 100.000 de dolares en la Loteria")
                self.Dinero=self.Dinero+100001
                self.Dinero=self.Dinero-1
                dinero='Dinero: '
                dinero+=str(self.Dinero)
                self.Money.config(text=dinero)
        if Xr==737373:
            mb.showinfo("Ganaste","Has ganado 1.000.000 de dolares en la Loteria")
            self.Dinero=self.Dinero+1001001
            self.Dinero=self.Dinero-1001
            dinero='Dinero: '
            dinero+=str(self.Dinero)
            self.Money.config(text=dinero)



aplicacion1=Aplicacion()
