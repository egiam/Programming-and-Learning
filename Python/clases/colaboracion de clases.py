
#ejercicio
class socio:

    def __init__(self):
        self.socio=input('Nombre del socio: ')
        self.socioant=int(input('antiguedad del socio: '))

    def antiguo(self):
        return self.socioant

    def returnname(self):
        return self.socio


class club:

    def __init__(self):
        self.socio1=socio()
        self.socio2=socio()
        self.socio3=socio()

    def Mantiguo(self):
        print('El socio mas antiguo es: ')
        if self.socio1.antiguo()>self.socio2.antiguo() and self.socio1.antiguo()>self.socio3.antiguo():
            print(self.socio1.returnname())
        elif self.socio2.antiguo()>self.socio3.antiguo():
            print(self.socio2.returnname())
        else:
            print(self.socio3.returnname())
        print('__________________________________________________________________________________________________________________')


clubtaiere=club()
clubtaiere.Mantiguo()


#Ejemplo2
import random


class Dado:

    def tirar(self):
        self.valor=random.randint(1,6)

    def imprimir(self):
        print("Valor del dado:",self.valor)

    def retornar_valor(self):
        return self.valor


class JuegoDeDados:

    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor()==self.dado3.retornar_valor():
            print("Gano")
        else:
            print("Perdio")


juego_dados=JuegoDeDados()
juego_dados.jugar()

#Ejemplo1
class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto

    def extraer(self,monto):
        self.monto=self.monto-monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre,"tiene depositado la suma de",self.monto)


class Banco:

    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero del banco es:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


banco1=Banco()
banco1.operar()
banco1.depositos_totales()
