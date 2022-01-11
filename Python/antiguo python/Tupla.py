#list sirve para cambiar una tupla a una lista, tuple para cambiar una lista a una tupla
#sep sirve para definir con que icono separar las destintas partes de una tupla o lista
#tupla es cuando va entre parentecis, la misma es inmutable, es decir no puede cambiar su contenido
#forma de recorrer una lista=for elemento in lista:


#lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.Nombre del empleado con sueldo mayor.Cantidad de empleados con sueldo menor a 1000.
def empleado():
    empleado=[]
    for x in range(5):
        nom=input("ingrese el nombre del empleado: ")
        sueldo=int(input("ingrese el sueldo del mismo: "))
        empleado.append((nom,sueldo))
    print(empleado)
    return empleado

def smayor(empleado):
    mayor=empleado[0]
    for elemento in empleado:
        if elemento[1]>mayor[1]:
            mayor=elemento
    print("Empleado con mayor sueldo:",mayor[0],"su sueldo es:",mayor[1])

def menor_1000(empleado):
    x=0
    m=[]
    for elemento in empleado:
        if elemento[1]<1000:
            x=x+1
            m.append(elemento[0])
    print("cantidad de personas con sueldo menor a 1000:",x,"nombres:",m)


empleado=empleado()
smayor(empleado)
menor_1000(empleado)

#nueva forma de usar el 'for' en listas
def cargar():
    lista=[]
    for x in range(5):
        num=int(input("Ingrese un valor:"))
        lista.append(num)
    return lista

def imprimir(lista):
    print("Lista completa")
    for elemento in lista:
        print(elemento)

def mayor(lista):
    may=lista[0]
    for elemento in lista:
        if elemento>may:
            may=elemento
    print("El elemento mayor de la lista es",may)

def sumar_elementos(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("La suma de todos sus elementos es",suma)


lista=cargar()
imprimir(lista)
mayor(lista)
sumar_elementos(lista)



#empleados y sus últimos tres sueldos. monto total cobrado por cada empleado. nombres de empleados que tuvieron un ingreso trimestral mayor a 10000
def cargar_empleados():
    empleados=[]
    for x in range(5):
        nom=input("Ingrese el nombre del empleado:")
        su1=int(input("Primer sueldo:"))
        su2=int(input("Segundo sueldo:"))
        su3=int(input("Tercer sueldo:"))
        empleados.append([nom,(su1,su2,su3)])
    return empleados


def ganancias(empleados):
    print("Monto total ganado por empleado en los ultimos tres meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0],total)


def ganancias_superior10000(empleados):
    print("Empleados con ingresos superiores a 10000 en los ultimos 3 meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print(empleados[x][0],total)


empleados=cargar_empleados()
ganancias(empleados)
ganancias_superior10000(empleados)



#pais mayor poblacion
def cargar_paisespoblacion():
    paises=[]
    for x in range(5):
        nom=input("Ingresar el nombre del pais:")
        cant=int(input("Ingrese la cantidad de habitantes:"))
        paises.append((nom,cant))
    return paises


def imprimir(paises):
    print("Paises y su poblacion")
    for x in range(len(paises)):
        print(paises[x][0],paises[x][1])


def pais_maspoblacion(paises):
    pos=0
    for x in range(1,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("Pais con mayor cantidad de habitantes:",paises[pos][0])


# bloque principal

paises=cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises)



#Cargar una lista de 5 enteros. Retornar el mayor y menor valor de la lista mediante una tupla.

def lista():
    lista=[]
    for x in range(5):
        v=int(input("ingrese un valor:"))
        lista.append(v)
    print(lista)
    return (lista)

def mayor(lista):
    mayor=lista[0]
    for x in range(1,5):
        if lista[x]>mayor:
            mayor=lista[x]
    print(mayor)
    return (mayor)

def menor(lista):
    menor=lista[0]
    for x in range(1,5):
        if lista[x]<menor:
            menor=lista[x]
    print(menor)
    return (menor)

def mayormenor(mayor,menor):
    ma=mayor
    me=menor
    return (ma,me)


lista=lista()
mayor=mayor(lista)
menor=menor(lista)
mayormenor=mayormenor(mayor,menor)
print(mayormenor)


#Definir una tupla con tres valores Convertir el contenido de la tupla a tipo lista. Modificar la lista y luego convertir la lista en tupla.
#mi forma
def valores():
    v1=int(input("ingrese valor: "))
    v2=int(input("ingrese valor: "))
    v3=int(input("ingrese valor: "))
    return (v1,v2,v3)

def lista(valor):
    lista=[]
    lista.append(valor[0])
    lista.append(valor[1])
    lista.append(valor[2])
    x=1
    aux=lista[x]
    lista[x]=lista[x+1]
    lista[x+1]=aux
    return (lista)

def tupla(lista):
    va1=lista[0]
    va2=lista[1]
    va3=lista[2]
    return (va1,va2,va3)


valor=valores()
print(valor)
lista=lista(valor)
print(lista)
tupla=tupla(lista)
print(tupla)

#otro forma
fechatupla1=(25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatupla1)
fechalista=list(fechatupla1)
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)
fechalista[0]=31
print("Imprimimos la lista ya modificada")
print(fechalista)
fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)



#Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe retornar.y mostrarla por pantalla.

def cargar_fecha():
    dd=int(input("Ingrese numero de dia:"))
    mm=int(input("Ingrese numero de mes:"))
    aa=int(input("Ingrese numero de año:"))
    return (dd,mm,aa)


def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")


# bloque principal

fecha=cargar_fecha()
imprimir_fecha(fecha)
