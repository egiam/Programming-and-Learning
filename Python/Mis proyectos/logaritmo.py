
class Logaritmo:

    def __init__(self):
        self.log=int(input("Defina cual es el logaritmo: "))
        self.X=int(input("Defina el resultado que tiene que dar el exponencial X del logaritmo anterior: "))
        self.Calculo()

    def Calculo(self):
        x=1
        while x!=0:
            z=self.X**(1/x)
            if z==self.log:
                print("RTA:",x)
                x=0
            else:
                x=x+1


log=Logaritmo()
