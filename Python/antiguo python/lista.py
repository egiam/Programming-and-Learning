"""
Listas: carga por teclado de componentes de tipo lista
"""

#lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

lista1=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista1.append(valor)

print("Lista original")
print(lista1)

lista2=[]
posicion=0
while posicion<len(lista1):
    if lista1[posicion]>=10:
        lista2.append(lista1.pop(posicion))
    else:
        posicion=posicion+1

print("Lista despues de borrar los elementos mayores o iguales a 10")
print(lista1)
print("Lista generada con los elementos mayores o iguales a 10")
print(lista2)

#empleados y sueldos borrando a empleados con sueldo mayor a 10000
empleado=[]
sueldo=[]
n=int(input("numero de empleados:"))
for x in range(n):
    emp=input("nombre del empleado:")
    suel=int(input("sueldo del mismo:"))
    empleado.append(emp)
    sueldo.append(suel)

cant=0
while cant<len(sueldo):
    if sueldo[cant]>=10000:
        sueldo.pop(cant)
        empleado.pop(cant)
    else:
        cant=cant+1

print("la lista es")
for x in range(len(sueldo)):
    print(empleado[x],sueldo[x])

#eliminar elemento igual a 5 de la lista
lista=[]
for x in range(10):
    list=int(input("numero:"))
    lista.append(list)

print(lista)

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1

print("la lista es",lista)

#Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la lista.
lista=[10, 20, 30, 40, 50]

print(lista)

lista.pop(0)
lista.pop(1)
lista.pop(2)

print(lista)

#problema mas
lista=[]
cant=1
for k in range(50):
    lista.append([])
    valor=1
    for x in range(cant):
        lista[k].append(valor)
        valor=valor+1
    cant=cant+1

print("elementos de la lista")
print(lista)

#un problema mas
empleados=[]
faltas=[]
for k in range(3):
    emp=input("nombre de empleado:")
    empleados.append(emp)
    num=int(input("numero de faltas del empleado en el mes:"))
    faltas.append([])
    for x in range(num):
        falt=int(input("dia de falta:"))
        faltas[k].append(falt)

print("Nombres de empleados y dias que falto")
for k in range(3):
    print(empleados[k])
    for x in range(len(faltas[k])):
        print(faltas[k][x])

men=len(faltas[0])
for x in range(1,3):
    if len(faltas[x])<men:
        men=len(faltas[x])

print("empleado/s que faltaron menos")
for x in range(3):
    if len(faltas[x])==men:
        print(empleados[x])


#temperatura media trimestral de cuatro paises. con las temperaturas medias mensuales de dichos paises.

paises=[]
temperaturas=[]
promediotemp=[]

for x in range(4):
    nom=input("Ingrese el nombre del pais:")
    paises.append(nom)
    temp1=int(input("Ingrese primer temperatura:"))
    temp2=int(input("Ingrese segunda temperatura:"))
    temp3=int(input("Ingrese tercer temperatura:"))
    temperaturas.append([temp1, temp2, temp3])

print("Paises y temperaturas medias de los ultimos tres meses mensuales")
for x in range(4):
    print(paises[x],temperaturas[x][0],temperaturas[x][1],temperaturas[x][2])

for x in range(4):
    pro=(temperaturas[x][0]+temperaturas[x][1]+temperaturas[x][2])//3
    promediotemp.append(pro)

print("Paises y temperaturas medias trimestrales")
for x in range(4):
    print(paises[x],promediotemp[x])

posmayor=0
for x in range(1,4):
    if promediotemp[x]>promediotemp[posmayor]:
        posmayor=x
print("Pais con temperatura media trimestral mayor:", paises[posmayor])
#dos listas de 3 elementos, una con padre y madre y otra con hijos, colocar el nombre del padre solo con la cantidad de hijos del mismo
padres=[]
hijos=[]
for k in range(3):
    pa=input("Ingrese el nombre del padre:")
    ma=input("Ingrese el nombre de la madre:")
    padres.append([pa, ma])
    cant=int(input("Cuantos hijos tienen esta familia:"))
    hijos.append([])
    for x in range(cant):
        nom=input("Ingrese el nombre del hijo:")
        hijos[k].append(nom)

print("Listado del padre, madre y sus hijos")
for k in range(3):
    print("Padre:",padres[k][0])
    print("Madre:",padres[k][1])
    for x in range(len(hijos[k])):
        print("Hijo:",hijos[k][x])

print("Listado del padre y cantidad de hijos que tiene")
for x in range(3):
    print("padre:",padres[x][0])
    print("Cantidad de hijos:",len(hijos[x]))

#El primer valor indica la cantidad de elementos que crearemos en la lista. El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
lista=[]
elementos=int(input("Cuantos elementos tendra la lista:"))
sub=int(input("Cuantos elementos tendran las listas internas:"))
for k in range(elementos):
    lista.append([])
    for x in range(sub):
        valor=int(input("Ingrese valor:"))
        lista[k].append(valor)

print(lista)

suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]

print("La suma de todos sus elementos:",suma)

#3 empleados con su sueldo (x mes) en los ultimos 3 meses (con doble resultado)
empleado=[]
sueldo=[]
I_total=[]
suma=0
for x in range(3):
    emp=input("ingrese nombre del empleado:")
    empleado.append(emp)
    sue1=int(input("ingrese sueldo del 1er mes del empleado:"))
    sue2=int(input("ingrese sueldo del 2do mes del empleado:"))
    sue3=int(input("ingrese sueldo del 3er mes del empleado:"))
    sueldo.append([sue1,sue2,sue3])
    suma=sue1+sue2+sue3
    print("la suma de los 3 sueldo es")
    print(suma)
    I_total.append(suma)

print("los empleados junto a sus sueldos son")
for x in range(3):
    print(empleado[x],sueldo[x][0],sueldo[x][1],sueldo[x][2])
    print("el ingreso toral del empleado en los 3 meses es")
    print(I_total[x])

#primera posibilidad (ideada por mi)
print("el empleado con mayor sueldo total fue")

if I_total[0]>I_total[1] and I_total[0]>I_total[2]:
    print(empleado[x])
else:
    if I_total[1]>I_total[0] and I_total[1]>I_total[2]:
        print(empleado[x])
    else:
        print(empleado[x])

#segunda posibilidad (dada por pythonya)
posmayor=0
mayor=totalsueldos[0]
for x in range(1,3):
    if totalsueldos[x]>mayor:
        mayor=totalsueldos[x]
        posmayor=x
print("Empleado con mayores ingresos en los ultimos tres meses")
print(nombres[posmayor])
print("con un ingreso de",mayor)

#lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela.
nombres=[]
notas=[]
for x in range(3):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    no1=int(input("Ingrese la primer nota:"))
    no2=int(input("Ingrese la segunda nota:"))
    notas.append([no1,no2])

for x in range(3):
    print(nombres[x],notas[x][0],notas[x][1])



"""
Listas: componentes de tipo lista
"""

#lista fijando 0 a valores mayor a 50
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)
for k in range(len(lista)):
    for x in range(len(lista[k])):
        if (lista[k][x])>50:
            lista[k][x]=0

print(lista)

#lista con 5 listas sumanodo cada elemento
lista=[[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]

suma1=0
for k in range(len(lista)):
    suma=0
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
    print("la suma de la lista es")
    print(suma)
    suma1=suma1+suma
print("la suma total es")
print(suma1)

#una lista con dos seblistas sumandose
lista=[[1,1,1,1,1], [2,2,2,2,2]]

print("la suma de las listas es")
for k in range(len(lista)):
    suma=0
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
    print(suma)

#lista por asignación. La lista tiene cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# imprimimos la lista completa
print(lista)
print("---------")
# imprimimos la primer componente
print(lista[0])
print("---------")
# imprimimos la primer componente de la lista contenida
# en la primer componente de la lista principal
print(lista[0][0])
print("---------")
# imprimimos con un for la lista contenida en la primer componente
for x in range(len(lista[0])):
    print(lista[0][x])
print("---------")
# imprimimos cada elemento entero de cada lista contenida en la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])


"""
listas, ordenamiento con listas paralelas
"""

#nombres de 5 países y cantidad de habitantes del mismo.
paises=[]
habitantes=[]
for x in range(5):
    pa=input("pais:")
    paises.append(pa)
    hab=int(input("habitantes del pais:"))
    habitantes.append(hab)

for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1

print("ordenado alfabeticamente")
for x in range(5):
    print(paises[x],habitantes[x])

for k in range(4):
    for x in range(4-k):
        if habitantes[x]<habitantes[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1


print("ordenado por habitantes")
for x in range(5):
    print(paises[x],habitantes[x])

#programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas de mayor a menor.
alumnos=[]
notas=[]
for x in range(5):
    nom=input("Ingrese el nombre del alumno:")
    alumnos.append(nom)
    no=int(input("Ingrese la nota de dicho alumno:"))
    notas.append(no)

for k in range(4):
    for x in range(4-k):
        if notas[x]<notas[x+1]:
            aux1=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux1
            aux2=alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux2

print("Lista de alumnos y sus notas ordenadas de mayor a menor")
for x in range(5):
    print(alumnos[x],notas[x])


"""
lista, ordenamiento de sus elementos
"""

#crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición.
sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo:"))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Lista con el último elemento ordenado")
print(sueldos)


"""
listas paralelas
"""

#dos listas numericas de 4 elementos con tercera lista echa por suma de los elementos de misma posicion de las otras dos Listas
numero1=[]
numero2=[]
for x in range(4):
    num1=float(input("numero:"))
    numero1.append(num1)
    num2=float(input("numero:"))
    numero2.append(num2)

print("listas de numeros")
print(numero1)
print(numero2)

suma=[]
for x in range(4):
    suma1=numero1[x]+numero2[x]
    suma.append(suma1)

print("lista con las sumas")
print(suma)

#programa de notas de alumnos + conducta etc
alumno=[]
nota=[]
for x in range(4):
    alu=input("nombre de alumno:")
    alumno.append(alu)
    note=float(input("nota del mismo:"))
    nota.append(note)

condicion=[]
for x in range(4):
    if nota[x]>=8:
        condicion.append("muy bueno")
    else:
        if nota[x]<=7 and nota[x]>=4:
            condicion.append("bueno")
        else:
            condicion.append("insuficiente")

print("las listas de alumnos, notas, y su condiciones respectivamente son")
print(alumno)
print(nota)
print(condicion)
print("alumnos con condicion de muy bueno")
for x in range(4):
    if condicion[x]=="muy bueno":
        print(alumno[x])
#programa con producto y precio mostrando cuales tienen precio mayor al primero
producto=[]
precio=[]
for x in range(5):
    pro=input("ingrese el nombre del producto:")
    producto.append(pro)
    pre=float(input("ingrese el precio del producto:"))
    precio.append(pre)

print("listas de producto y precio respectivamente")
print(producto)
print(precio)
cantidad=0
productos=[]
precios=[]
print("cantidad de productos con precio mayor al primero")
for x in range(1,5):
    if precio[0]<precio[x]:
        cantidad=cantidad+1
        productos.append(producto[x])
        precios.append(precio[x])
print(cantidad)
print("nombre de los productos")
print(productos)
print("precio de los mismos")
print(precios)

#programa que permite cargar 5 nombres y sus edades respectivas, imprimiendo los nombres de los mayores de edad
nombres=[]
edades=[]
for x in range(5):
    nom=input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed=int(input("Ingrese la edad de dicha persona:"))
    edades.append(ed)

print("Nombre de las personas mayores de edad:")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])


"""
lista mayor y menor elemento
"""

#lista de 5 nombres, mostrar nombre menor en orden alfabetico
nombres=[]
for x in range(5):
    nombre=input("ingrese nombre:")
    nombres.append(nombre)

n_menor=nombres[0]  #nombre menor, no valor.
for x in range(1,5):
    if nombres[x]<n_menor:
        n_menor=nombres[x]

print("la lista es")
print(nombres)
print("el nombre menor de la lista es")
print(n_menor)

#lista de 5 enteros, identificando el mayor y dando un mensaje si se encuentra en 2 o mas posiciones
lista=[]
for x in range(5):
    valor=int(input("ingrese valor:"))
    lista.append(valor)

mayor=lista[0]
posicion=0
igual=0
for x in range(1,5):
    if lista[x]==mayor:
        mayor=lista[x]
        igual=x
    if lista[x]>mayor:
        mayor=lista[x]
        posicion=x

print("la lista es")
print(lista)
if igual==0:
    print("la posicion del mayor es")
    print(posicion)
else:
    if igual>0:
        print("el mayor de la lista se repite dos o mas veces en las posiciones:")
        print(igual)
        print(posicion)

#lista de 5 enteros, identificando el menor de esta y su posicion
lista=[]
for x in range(5):
    valor=int(input("valor de un elemento:"))
    lista.append(valor)

menor=lista[0]
posicion=0
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x

print("lista completa")
print(lista)
print("menor de la lista")
print(menor)
print("posicion del menor")
print(posicion)

#lista con 5 enteros, identificando el mayor de la lista
lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=len(lista[x])

print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor)


"""
carga por teclado de lista
"""

#dos turnos y 8 empleados
temprano=[]
tarde=[]
for x in range(4):
    sueldo1=int(input("sueldo de empleados de turno temprano:"))
    sueldo2=int(input("sueldo de empleados de turno tarde:"))
    temprano.append(sueldo1)
    tarde.append(sueldo2)
print("sueldos de turno temprano")
print(temprano)
print("sueldos de turno tarde")
print(tarde)

#alturas con promedio
suma=0
mayor_avg=0
menor_avg=0
igual_avg=0

list4=[]
for x in range(5):
    altura=float(input("colocar la altura:"))
    list4.append(altura)
    suma=suma+altura
promedio=round(suma/5,2)

for x in range(5):
    if list4[x]>promedio:
        mayor_avg=mayor_avg+1
    else:
        if list4[x]<promedio:
            menor_avg=menor_avg+1
        else:
            if list4[x]==promedio:
                igual_avg=igual_avg+1
print("el promedio de las alturas es")
print(promedio)
print("las personas con una altura mayor al promedio son")
print(mayor_avg)
print("las personas con una altura menor al promedio son")
print(menor_avg)
if igual_avg>0:
    print("las personas con una altura igual al promedio son")
    print(igual_avg)

#sueldos con su promedio
suma=0
lista=[]
for x in range(5):
    sueldo=float(input("coloque el sueldo:"))
    lista.append(sueldo)
    suma=suma+sueldo
promedio=suma/5
print("la suma de los 5 sueldos es")
print(suma)

print(lista)
print("el promedio de los sueldos es")
print(promedio)

#un problema
list1=[]
valor=float(input("ingrese un valor(0 para finalizar):"))
while valor!=0:
    list1.append(valor)
    valor=float(input("ingrese un valor:"))
print("la lista es")
print(len(list1))


#definimos una lista vacia
list2=[]
#disponemos un ciclo de 5 vueltas
for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    list2.append(valor)

#imprimimos la lista
print(lista)


"""
Listas y algunas funciones
"""

#nombres con 5 o mas caracteres
nombres=["eze","joa","matsae","latesa","mitre"]
suma=0
x=0
while x<len(nombres):
    if len(nombres[x])>=5:
        suma=suma+1
    x=x+1
print("la cantidad de nombres con 5 o mas caracteres es")
print(suma)

#lista de 5 mostrando solo valores igual o mayor a 7
list3=[2,6,8,7,9]
x=0
while x<len(list3):
    if list3[x]>=7:
        print(list3[x])
    x=x+1

#lista de 8 elementos definiendo cuantos son mayores a 100
list2=[123,12,123,23,345,23,34,23]
suma=0
x=0
while x<len(list2):
    if list2[x]>=100:
        suma=suma+1
    x=x+1
print(list2)
print("cantidad de valores mayor a 100")
print(suma)

#lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
lista=[10,7,3,7,2]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x=x+1
print("Los elementos de la lista son")
print(lista)
print("La suma de todos sus elementos es")
print(suma)

#lista de los meses
list1=["Enero","Febrero","Marzo","Abril"]
print("el mes 1 y 4 es")
print(list1[0])
print(list1[3])
print(list1)

#alumno y sus notas en listas
lista1=["joa",2,10]
print("nombre de alumno:")
print(lista1[0])
promedio=(lista1[1]+lista1[2])//2
print("promedio:")
print(promedio)
