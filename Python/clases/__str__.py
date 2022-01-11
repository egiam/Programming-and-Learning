
#ejercicio
class Jugador:

    def __init__(self,nombre,puntaje):
        self.nombre=nombre
        self.puntaje=puntaje

    def __str__(self):
        cadena=self.nombre+"-"
        if self.puntaje>1000:
            cadena=cadena+'experto'
        else:
            cadena=cadena+'principiante'
        return cadena


jugador1=Jugador('Damian',1020)
jugador2=Jugador('Mamerto',989)
jugador3=Jugador('Murphy',7808)

print(jugador1)
print(jugador2)
print(jugador3)


#Ejemplo2
class Familia:

    def __init__(self,padre,madre,hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    def __str__(self):
        cadena=self.padre+","+self.madre
        for hi in self.hijos:
            cadena=cadena+","+hi
        return cadena


familia1=Familia("Pablo","Ana",["Pepe","Julio"])
familia2=Familia("Jorge","Carla")
familia3=Familia("Luis","Maria",["marcos"])

print(familia1)
print(familia2)
print(familia3)

#Ejemplo1
class Punto:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"



punto1=Punto(10,3)
punto2=Punto(3,4)
print(punto1)
print(punto2)
