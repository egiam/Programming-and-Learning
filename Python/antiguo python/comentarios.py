"""
Mostrar la tabla de 5 con las escrituras repetitivas:
 while
 y
 for
"""


#utilizando el while
print("tabla del 5 empleando while")
x=5
while x<=50:
    print(x)
    x=x+5


#utilizando el for
print("tabla del 5 empleando el for")
for x in range(5,51,5):
    print(x)


"""
Suma de valores enteros
"""

suma=0
valor=int(input("Ingrese valor (-1 finaliza):"))     # se carga el primer valor antes del while
while valor!=-1:
    suma=suma+valor
    valor=int(input("Ingrese valor(-1 finaliza):"))  # se cargar todos los otros valores dentro del while
print("La suma de los valores ingresados es")
print(suma)


"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma.
"""

#Programa: Carga de 10 valores
#Programador: Ezequiel Giampaoli
#Ultima modificacion: 18/7/2019
suma=0
for x in range(10):
    valor=float(input("valor numerico:"))   #se ingresa el valor para la Suma
    suma=suma+valor
print("el resultado de la suma es")         #se coloca el resultado de la Suma
print(suma)
