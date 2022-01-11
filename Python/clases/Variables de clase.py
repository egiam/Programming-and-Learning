
#ejercicio
import random
class Jugador:

    Tiempo=30

    def __init__(self,nombre,puntaje):
        self.nombre=nombre
        self.puntaje=puntaje

    def suma_puntaje(self):
        self.puntaje=self.puntaje+random.randint(1,500)

    def imprimir(self):
        print(self.nombre,self.puntaje,sep='/')

    def pasar_tiempo(self):
        Jugador.Tiempo=Jugador.Tiempo-5



jugador1=Jugador('Egiam',0)
jugador2=Jugador('TatinPlay',0)
jugador3=Jugador('Gambalest',0)
jugador4=Jugador('Lcristori',0)
jugador5=Jugador('Ngiampaoli',0)
jugador6=Jugador('Lgiampaoli',0)


while Jugador.Tiempo>0:
    jugador1.suma_puntaje()
    jugador2.suma_puntaje()
    jugador3.suma_puntaje()
    jugador4.suma_puntaje()
    jugador5.suma_puntaje()
    jugador6.suma_puntaje()
    print('_____________________________________')

    jugador1.pasar_tiempo()
    print('_____________________________________')

    jugador1.imprimir()
    jugador2.imprimir()
    jugador3.imprimir()
    jugador4.imprimir()
    jugador5.imprimir()
    jugador6.imprimir()
    print('_____________________________________')

    print('Tiempo restante: ',Jugador.Tiempo)
    print('_____________________________________')

print('Puntuaciones Finales: ')

jugador1.imprimir()
jugador2.imprimir()
jugador3.imprimir()
jugador4.imprimir()
jugador5.imprimir()
jugador6.imprimir()
print('_____________________________________')


#Ejemplo1
class Cliente:
    suspendidos=[]

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre:",self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)



cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)
