
class Fabrica():
    def __init__(self,tipo,color,precio):
        self.tipoLl = tipo
        self.color = color
        self.precio = precio

    def Llantas(self):
        print("Las llantas son tipo: ",self.tipoLl)

    def Color(self):
        print("El color es: ",self.color)

    def Precio(self):
        print("El precio es: ",self.precio)

class Moto(Fabrica):
    pass

class Auto(Fabrica):
    pass

moto = Moto("mamacho","beige",1233)
moto.Llantas()
moto.Color()
moto.Precio()

auto = Auto("muncio","rojo",2300)
auto.Llantas()
auto.Color()
auto.Precio()
