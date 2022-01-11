
#Funciones para el string en print

Functions = [".upper()",".lower()",".islower()",".isupper()",""]
#Podes usarlos seguidos a traves de puntos.

sentencia = "mama mia"

print("La cantidad de letras en esa sentencia es de: " + str(len(sentencia)))

#remplazar una palabra
print(sentencia.replace("mama","ama"))


#importes
from math import *

edad = int(input("Ingrese su edad: "))

print(f"Your age is {edad}")

#Funciones para numeros
#Functions.append("max()","min()","pow(num,num)","round()","abs()","sqrt(num)","factorial(num)")

#Redondea hacoa arriba
Functions.append("ceil(num)")


def Retomando_Funciones():
    print("Retomo la funcion")
    x = 3
    z = 0
    while x > 0:
        print(f"Numero {x}")
        x = x - 1
    for x in range(10):
        print(x)

Retomando_Funciones()

def retornado():
    z = 5
    return z

numero = retornado()


for x in Functions:
    print(x)

