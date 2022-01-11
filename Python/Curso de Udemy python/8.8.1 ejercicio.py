
class Calculadora():
    def __init__(self):
        self.V1 = float(input("Coloque un numero: "))
        self.V2 = float(input("Coloque otro numero: "))

    def suma(self):
        self.pluss = self.V1+self.V2
        print("La suma de ambos numeros es: ",pluss)

    def resta(self):
        self.rest = self.V1-self.V2
        print("La resta de ambos numeros es: ",rest)

    def multiplicacion(self):
        self.potencia = self.V1*self.V2
        print("La potencia de ambos numeros es: ",potencia)

    def division(self):
        self.Div = self.V1/self.V2
        print("La divisionde ambos numeros es: ",Div)

x = 0
while x != 1:
    z = int(input("Quieres salir[1], sumar[2], restar[3], multiplicar[4] o dividir[5]: "))
    if z == 1:
        print("A finalizado con el programa")
        break
    elif z == 2:
        calc = Calculadora()
        calc.suma()
    elif z == 3:
        calc = Calculadora()
        calc.resta()
    elif z == 4:
        calc = Calculadora()
        calc.multiplicacion()
    elif z == 5:
        calc = Calculadora()
        calc.division()
    else:
        print("por favor coloque el numero correspondiente")
