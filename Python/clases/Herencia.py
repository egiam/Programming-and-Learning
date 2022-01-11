#mi ejercicio
class Celular:

    def __init__(self):
        self.Ram=8
        self.Mem=256
        self.x=0
        self.z=0

    def Memoria_total(self):
        print(self.Ram,'De memoria Ram')
        print(self.Mem,'De memoria de disco')

    def imprimir(self):
        print(self.x,self.Ram,sep='/')
        print(self.z,self.Mem,sep='/')

    def Memoria_ocupada(self):
        pass

class MemoriaRam(Celular):

    def Memoria_ocupada(self,ocupado):
        super().__init__()
        self.x=self.Ram-ocupado
        print('Memoria libre:',self.x,'de',self.Ram)

class MemoriaGb(Celular):

    def Memoria_ocupada(self,ocupado):
        self.z=self.Mem-ocupado
        print('Memoria libre:',self.z,'de',self.Mem)



memoriaR=MemoriaRam()
memoriaG=MemoriaGb()
memoriaR.Memoria_ocupada(3)
memoriaG.Memoria_ocupada(109)
print('Memoria')
memoriaG.imprimir()
memoriaR.imprimir()

#otra forma de resolver el ejercicio, version pythonya
class Cuenta:

    def __init__(self,titular,monto):
        self.titular=titular
        self.monto=monto

    def imprimir(self):
        print("Titular:",self.titular)
        print("Monto:",self.monto)


class CajaAhorro(Cuenta):

    def __init__(self,titular,monto):
        super().__init__(titular,monto)

    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super().imprimir()

class PlazoFijo(Cuenta):

    def __init__(self,titular,monto,plazo,interes):
        super().__init__(titular,monto)
        self.plazo=plazo
        self.interes=interes

    def imprimir(self):
        print("Cuenta de plazo fijo")
        super().imprimir()
        print("Plazo en dias:",self.plazo)
        print("Interes:",self.interes)
        self.ganancia_interes()

    def ganancia_interes(self):
        ganancia=self.monto*self.interes/100
        print("Importe del interes:",ganancia)


cajaahorro=CajaAhorro("Juan", 2000)
cajaahorro.imprimir()

plazofijo=PlazoFijo("Diego", 10000, 30, 0.75)
plazofijo.imprimir()




#ejercicio
class Cuenta:

    def inicializar(self):
        self.titular=input('Nombre del titular de la cuenta: ')
        self.monto=0

    def depositar(self):
        x=float(input('Monto a depositar: '))
        self.monto=self.monto+x

    def imprimir(self):
        print('Cuenta:')
        print(self.titular,self.monto)

    def intereses(self):
        pass

class CajaAhorra(Cuenta):

    def intereses(self):
        pass

class PlazoFijo(Cuenta):

    def intereses(self,numero):
        if numero>30:
            print('Interes generado cada 30 dias del 15% ')
            x=numero//30
            for k in range(x):
                self.monto=self.monto+self.monto*0.15
                print(self.monto)
            print('Monto total al',x,'mes',self.monto)
        elif numero==30:
            print('Interes generado total del 10% ')
            self.monto=self.monto+self.monto*0.1
            print(self.monto)
        elif numero<30 and numero>10:
            print('interes generado total del 5% ')
            self.monto=self.monto+self.monto*0.05
            print(self.monto)
        elif numero<10:
            print('Interes generado total del 2,5% ')
            self.monto=self.monto+self.monto*0.025
            print(self.monto)




cajaA=CajaAhorra()
plazoF=PlazoFijo()

decidir=int(input('Desea entrar a la caja de ahorros o al plazo fijo [1/2]: '))
if decidir==1:
    cajaA.inicializar()
    cajaA.depositar()
    cajaA.imprimir()
elif decidir==2:
    plazoF.inicializar()
    plazoF.depositar()
    numero=int(input('Que cantidad de dias desea mantener el dinero en el plazo fijo: '))
    plazoF.intereses(numero)
    plazoF.imprimir()


#Ejemplo1
class Operacion:

    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0

    def cargar1(self):
        self.valor1=int(input("Ingrese primer valor:"))

    def cargar2(self):
        self.valor2=int(input("Ingrese segundo valor:"))

    def mostrar_resultado(self):
        print(self.resultado)

    def operar(self):
        pass


class Suma(Operacion):

    def operar(self):
        self.resultado=self.valor1+self.valor2


class Resta(Operacion):

    def operar(self):
        self.resultado=self.valor1-self.valor2


suma1=Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
print("La suma de los dos valores es")
suma1.mostrar_resultado()

resta1=Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
print("La resta de los valores es:")
resta1.mostrar_resultado()

#Ejemplo2
class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre:")
        self.edad=int(input("Ingrese la edad:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)


class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")



persona1=Persona()
persona1.imprimir()
print("____________________________")
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
