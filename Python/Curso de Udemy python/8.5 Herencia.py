
class Animales():
    def __init__(self,descripcion,especie, hablar):
        self.descripcion = descripcion
        self.especie = especie
        self.hablar = hablar

    def habla(self):
        print("yo hago: ",self.hablar)

    def describir(self):
        print("yo soy la especie: ",self.especie)

class Perro(Animales):
    pass

class Abeja(Animales):
    def sonido(self,sonido):
        self.sonido = sonido
        print(self.sonido)


perro = Perro("Perro","Mamifero","Guau!")
perro.habla()
perro.describir()

abeja = Abeja("Abeja","Insecto","Brr!")
abeja.sonido("Brr!")
abeja.habla()
abeja.describir()
