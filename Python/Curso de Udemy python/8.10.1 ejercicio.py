
class Marino():
    def Hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def Hablar(self):
        print("Soy un pulpo")

class Foca(Marino):
    def Hablar(self,mensaje):
        self.mensaje = mensaje
        print(self.mensaje)


marino = Marino()
marino.Hablar()

pulpo = Pulpo()
pulpo.Hablar()

foca = Foca()
foca.Hablar("Hola, soy una foca")
