
class Animales():#clase padre
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self,mesnaje):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("yo hago Guau!")  #se modifica el valor de la funcion hablar en la clase padre

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Firulais","Guau!")
perro.hablar()

animales = [Perro("Firulais","Guau!"),Pez("Nemo","Nada")]

for i in animales:
    print(i.hablar())
