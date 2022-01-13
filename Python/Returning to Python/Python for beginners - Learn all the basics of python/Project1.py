
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
    

#para listas insert te permite insertar en cierto lugar algo
food = ["mama","papa","lala"]
prices = [1.22,2.11,3.44]

print(food)

food.insert(2,"juana")
#[mama,papa,juana,lala]

print(food)

food.extend(prices)

#Te da el posicionamiento en la lista 
print(food.index("lala"))

#cuenta cuantas veces el elemento esta repetido
print(food.count("lala"))

#copia
random = food.copy()+prices.copy()

print(random)

#borrar todo
food.clear()

print(food)

