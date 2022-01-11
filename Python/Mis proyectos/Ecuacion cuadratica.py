
class Aplicacion:

    def __init__(self):
        self.a=int(input("Coloque valor de a: "))
        self.b=int(input("Coloque valor de b: "))
        self.c=int(input("Coloque valor de c: "))
        self.cuadradoperfecto()

    def cuadradoperfecto(self):
        a=self.a
        b=self.b
        c=self.c
        A=2*a
        B1=-1*b
        if b<0:
            B2=(-1*b)**2
        else:
            B2=b**2
        C=-4*a*c
        D=(B2+C)**(1/2)

        X1=(B1+D)/A
        X2=(B1-D)/A

        print("El valor de x es:",X1,"y",X2)



aplicacion=Aplicacion()
