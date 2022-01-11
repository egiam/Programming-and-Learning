
"""
Redefinición de los operadores matemáticos con objetos
"""

#Ejemplo2
class Lista:

    def __init__(self, lista):
        self.lista=lista

    def imprimir(self):
        print(self.lista)

    def __add__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]+entero)
        return nueva

    def __sub__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]-entero)
        return nueva

    def __mul__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]*entero)
        return nueva

    def __floordiv__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]/entero)
        return nueva


lista1=Lista([3,4,5])
lista1.imprimir()
print(lista1+10)
print(lista1-10)
print(lista1*10)
print(lista1//10)

#Ejemplo1
class Cliente:

    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto

    def __add__(self,objeto2):
        s=self.monto+objeto2.monto
        return s

cli1=Cliente('Ana',1200)
cli2=Cliente('Luis',1500)
print("El total depositado por los dos clientes es")
print(cli1+cli2)
