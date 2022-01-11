
class Aplicacion:

    def __init__(self):
        self.a=int(input("Coloque el valor de a (Colocar 0 en caso de ser la incognita): "))
        self.b=int(input("Coloque el valor de b (Colocar 0 en caso de ser la incognita): "))
        self.c=int(input("Coloque el valor de c (Colocar 0 en caso de ser la incognita): "))
        elegir=input("Si quiere calcular el lado a presione 1\nSi quiere calcular el lado b presione 2\nSi quiere calcular el lado c presione 3\nEleccion: ")
        if elegir==1:
            self.ladoA()
        elif elegir==2:
            self.ladoB()
        elif elegir==3:
            self.ladoC()
        else:
            print("porfavor, coloque el numero correspondiente")

    def ladoA(self):
        A=int(input("Coloque el angulo A: "))
        b=self.b**2
        c=self.c**2
        if self.b>self.c:
            d=2*self.b*self.c*()
        elif self.c>self.b:
            d=2*self.b*self.c*


aplicacion=Aplicacion()
