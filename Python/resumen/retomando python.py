
"""
Declaración de una clase y creación de objetos
"""
 
#objetos

"""
Conceptos de programación orientada a objetos
"""

print("Programación Lineal: Es cuando desarrollamos todo el código sin emplear funciones. El código es una secuencia lineal de comando.")

print("Programación Estructurada: Es cuando planteamos funciones que agrupan actividades a desarrollar y luego dentro del programa llamamos a dichas funciones que pueden estar dentro del mismo archivo (módulo) o en una librería separada.")

print("Programación Orientada a Objetos: Es cuando planteamos clases y definimos objetos de las mismas (Este es el objetivo de los próximos conceptos, aprender la metodología de programación orientada a objetos y la sintaxis particular de Python para la POO)")

"""
Aplicaciones propias con varios módulos
"""

#Mas carpetas/archuvos
#Modulos

"""
Importar algunas funcionalidades de un módulo de la biblioteca estándar de Python
from random import randint,shuffle
"""

#ejercicio
from math import factorial

def numero_factorial():
    Val001=int(input("Ingrese un numero para calcular su factorial: "))
    Fact001=factorial(Val001)
    print('El factorial es: ',Fact001)

numero_factorial()


#Ejemplo1
from math import sqrt, pow

valor=int(input("Ingrese un valor entero:"))
r1=sqrt(valor)
r2=pow(valor,3)
print("La raiz cuadrada es",r1)
print("El cubo es",r2)

"""
Biblioteca estándar de Python
"""

#ejercicio2
import random

def N_aleatorios():
    aleatorios001=[]
    for x in range(5):
        aleatorios001.append(random.randint(1,3))
    return aleatorios001

def control(aleatorios):
    seguir='si'
    while seguir=='si':
        if aleatorios[0]==1:
            seguir='no'
        else:
            random.shuffle(aleatorios)
    print(aleatorios)

aleatorios001=N_aleatorios()
control(aleatorios001)


#ejercicio1
import random

def adivinar(numero):
    seguir='si'
    while seguir=='si':
        Ad=int(input('Adivine el numero del 1 al 100: '))
        if Ad==numero:
            print('Gano')
            seguir='no'
        elif Ad>numero:
            print('El numero aleatorio es menor')
        elif Ad<numero:
            print('El numero aleatorio es mayor')


numero=random.randint(1,100)
adivinar(numero)


#Ejemplo2
import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista


def imprimir(lista):
    print(lista)


def mezclar(lista):
    random.shuffle(lista)


lista=cargar()
print("Lista generada aleatoriamente")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar")
imprimir(lista)


#Ejemplo1/ simule tirar dos dados y luego muestre los valores que salieron. random
import random

dado1=random.randint(1,6)
dado2=random.randint(1,6)
print("Primer dado:",dado1)
print("Segundo dado:",dado2)
suma=dado1+dado2
if suma==7:
    print("Gano")
else:
    print("Perdio")

"""
Indices negativos en listas, tuplas y cadenas de caracteres
"""

#ejercicio
palabra=input("Ingresar una palabra:")
indice=-1
for x in range(len(palabra)):
    print(palabra[indice],end="")
    indice=indice-1


#Ejemplo1
def capicua(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es capicua")
    else:
        print("No es capicua")


capicua("neuquen")
capicua("casa")

"""
Porciones de listas, tuplas y cadenas de caracteres
"""

#ejercicio
def carga_lista():
    lista=[]
    for x in range(10):
        Num=int(input('Coloque un entero: '))
        lista.append(Num)
    return lista

def pri_mitad(lista):
    print('Primera mitad de la lista: ')
    lista1=lista[:5]
    print(lista1)



lista=carga_lista()
pri_mitad(lista)


#Ejemplo3
def primeros_tres(cadena):
    return cadena[:3];


meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
for x in meses:
    print(primeros_tres(x))


#Ejemplo2
def meses_faltantes(numeromes):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numeromes:]


print("Imprimir los nombres de meses que faltan hasta fin de año")
numeromes=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numeromes)
print(mesesfalta)


#Ejemplo1
lista1=[0,1,2,3,4,5,6]
lista2=lista1[2:5]
print(lista2) # 2,3,4
lista3=lista1[1:3]
print(lista3) # 1,2
lista4=lista1[:3]
print(lista4) # 0,1,2
lista5=lista1[2:]
print(lista5) # 2,3,4,5,6

"""
Funciones: parámetros mutables e inmutables
"""

def cargar():
    contactos={}
    continua="s"
    while continua=="s":
        nombre=input("Ingrese el nombre del contacto:")
        telefono=input("Ingrese el numero de telefono:")
        contactos[nombre]=telefono
        continua=input("Ingresa otro contacto[s/n]?:")
    return contactos


def modificar_telefono(contactos):
    nombre=input("Ingrese el nombre de contacto a modificar el telefono:")
    if nombre in contactos:
        telefono=input("Ingrese el nuevo numero telefonico")
        contactos[nombre]=telefono
    else:
        print("No existe un contacto con el nombre ingresado")


def imprimir(contactos):
    print("Listado de todos los contactos")
    for nombre in contactos:
        print(nombre,contactos[nombre])


contactos=cargar()
modificar_telefono(contactos)
imprimir(contactos)

"""
Diccionarios: con valores de tipo listas, tuplas y diccionarios
"""

#ejercicio
def Carga_alumno():
    Alumnos001={}
    for x in range(3):
        DNI=int(input('Identificacion del alumno/DNI: '))
        Name=input('Nombre del alumno: ')
        materias=[]
        seguir='s'
        while seguir=='s':
            Mat=input('Nombre de la materia: ')
            seguir001='s'
            Nota=[]
            while seguir001=='s':
                Not=float(input('Coloque una nota: '))
                Nota.append(Not)
                seguir001=input('Tiene mas notas [s/n]: ')
            materias.append((Mat,Nota))
            seguir=input('Tiene mas materias [s/n]: ')
        Alumnos001[DNI]=Name,materias
    for cant in Alumnos001:
        print(cant,Alumnos001[cant])
    return Alumnos001

def Consulta(Alumnos001):
    DNI=int(input('Coloque el DNI del alumno: '))
    if DNI in Alumnos001:
        print(Alumnos001[DNI])


Alumnos001=Carga_alumno()
seguir='s'
while seguir=='s':
    Consulta(Alumnos001)
    seguir=input('Quiere consultar por otro alumno [s/n]: ')



#Ejemplo1
def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codigo del producto:"))
        descripcion=input("Ingrese la descripcion:")
        precio=float(input("Ingrese el precio:"))
        stock=int(input("Ingrese el stock actual:"))
        productos[codigo]=(descripcion,precio,stock)
        continua=input("Desea cargar otro producto[s/n]?")
    return productos

def imprimir(productos):
    print("Listado completo de productos:")
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

def consulta(productos):
    codigo=int(input("Ingrese el codigo de articulo a consultar:"))
    if codigo in productos:
        print(productos[codigo][0],productos[codigo][1],productos[codigo][2])

def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])


productos=cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)

"""
Estructura de datos tipo diccionario
*utiliza una clave para acceder a un valor.
"""

#ejercicio
def Documento():
    ID={}
    seguir='s'
    while seguir=='s':
        Doc=int(input('Ingrese el numero de documento: '))
        Name=input('Ingrese el nombre: ')
        ID[Doc]=Name
        seguir=input('Quiere colocar otro documento: [s/n] ')
    return ID

def Listado_ID(ID):
    for cant in ID:
        print(cant,ID[cant])

def Consulta_ID(ID):
    Doc=int(input('Ingrese el documento: '))
    if Doc in ID:
        print('La persona es: ',ID[Doc])


ID=Documento()
Listado_ID(ID)
seguir='s'
while seguir=='s':
    Consulta_ID(ID)
    seguir=input('Quiere colocar otro documento: [s/n] ')


#Ejemplo3
def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("Ingrese palabra en castellano:")
        ing=input("Ingrese palabra en ingles:")
        diccionario[ing]=caste
        continua=input("Quiere cargar otra palabra:[s/n]")
    return diccionario


def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])


def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en ingles a consultar:")
    if pal in diccionario:
        print("En castellano significa:",diccionario[pal])



diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)


#Ejemplo2
def cargar():
    productos={}
    for x in range(5):
        nombre=input("Ingrese el nombre del producto:")
        precio=int(input("Ingrese el precio:"))
        productos[nombre]=precio
    return productos


def imprimir(productos):
    print("Listado de todos los articulos")
    for nombre in productos:
        print(nombre, productos[nombre])


def imprimir_mayor100(productos):
    print("Listado de articulos con precios mayores a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)



productos=cargar()
imprimir(productos)
imprimir_mayor100(productos)


#Ejemplo1
def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])


paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises)


"""
Variantes de la estructura repetitiva for para recorrer tuplas y listas
"""

#ejercicio
def Palabras001():
    palabras001=[]
    Cantidad=int(input('Cuantas palabras desea colocar: '))
    for x in range(Cantidad):
        Pal=input("Ingrese una palabra: ")
        palabras001.append(Pal)
    print('Palabras:')
    for cantidad in palabras001:
        print(cantidad)

    return palabras001

def masde5(palabras001):
    print('Palabras con mas de 5 caracteres:')
    for cantidad in palabras001:
        if len(cantidad)>5:
            print(cantidad)


palabras001=Palabras001()
masde5(palabras001)


#Ejemplo2
def cargar():
    empleados=[]
    for x in range(5):
        nombre=input("Nombre del empleado:")
        sueldo=int(input("Ingrese el sueldo:"))
        empleados.append((nombre,sueldo))
    return empleados


def imprimir(empleados):
    print("Listado de los nombres de empleados y sus sueldos")
    for nombre,sueldo in empleados:
        print(nombre,sueldo)


def mayor_sueldo(empleados):
    empleado=empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado=emp
    print("Empleado con mayor sueldo:",empleado[0],"su sueldo es",empleado[1])


def sueldos_menor1000(empleados):
    cant=0
    for empleado in empleados:
        if empleado[1]<1000:
            cant=cant+1
    print("Cantidad de empleados con un sueldo menor a 1000 son:",cant)



empleados=cargar()
imprimir(empleados)
mayor_sueldo(empleados)
sueldos_menor1000(empleados)


#Ejemplo1
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

"""
Listas y tuplas anidadas
"""

#ejercicio
def Trabajadores001():
    trabajadores001=[]
    for x in range(5):
        empleado001=input('Coloque nombre del empleado: ')
        trabajadores001.append(empleado001)
        sueldo1=float(input('Coloque el primer sueldo del empleado: '))
        sueldo2=float(input('Coloque el segundo sueldo del empleado: '))
        sueldo3=float(input('Coloque el tercer sueldo del empleado: '))
        trabajadores001.append((sueldo1,sueldo2,sueldo3))

    return trabajadores001

def total(trabajadores001):
    total=0
    k=1
    print('Monto total ganado por el empleado en los ultimos 3 meses:')
    for x in range(5):
        total=trabajadores001[k][0]+trabajadores001[k][1]+trabajadores001[k][2]
        print(trabajadores001[k-1],total,sep='/')
        if total>10000:
            print(trabajadores001[k-1],total,sep='$$$')
        k=k+2


trabajadores001=Trabajadores001()
x=0
while x<=8:
    print(trabajadores001[x],trabajadores001[x+1],sep='/')
    x=x+2
total(trabajadores001)


#Ejemplo2
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


paises=cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises)


#Ejemplo1
empleado=["juan", 53, (25, 11, 1999)]
print(empleado)
empleado.append((1, 1, 2016))
print(empleado)
alumno=("pedro",[7, 9])
print(alumno)
alumno[1].append(10)
print(alumno)

"""
Estructura de datos tipo Tupla
permite almacenar una colección de datos no necesariamente del mismo tipo.
Los datos de la tupla son inmutables a diferencia de las listas que son mutables.
"""

#ejercicio

def Lista001():
    lista001=[]
    for x in range(5):
        k=int(input("Coloque un numero: "))
        lista001.append(k)
    return lista001

def Mayor001(lista001):
    May001=lista001[0]
    Men001=lista001[0]
    for x in range(len(lista001)):
        if May001<lista001[x]:
            May001=lista001[x]
        else:
            if Men001>=lista001[x]:
                Men001=lista001[x]
    return (May001,Men001)


lista001=Lista001()
tupla001=Mayor001(lista001)
print("Numero mas grande: ")
print(tupla001[0],tupla001[1],sep='/')


#resuelto
def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese valor: "))
        lista.append(valor)
    return lista


def retornar_mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    return (may,men)


# bloque principal

lista=cargar()
mayor,menor=retornar_mayormenor(lista)
print("Mayor valor de la lista:",mayor)
print("Menor valor de la lists:",menor)


#Ejemplo de cambiar de tupla a lista y biceversa

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


#Ejemplo inicial

def cargar_fecha():
    dd=int(input("Ingrese numero de dia:"))
    mm=int(input("Ingrese numero de mes:"))
    aa=int(input("Ingrese numero de año:"))
    return (dd,mm,aa)


def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")       #sep=separar los elementos de la tupla con cierto caracter


fecha=cargar_fecha()
imprimir_fecha(fecha)

"""
Funciones: con cantidad variable de parámetros
(Para definir una cantidad variable de parámetros debemos anteceder el caracter asterísco (*) al último parámetro de la función.)
"""

#Desempaquetar una tupla
def sumar(v1, v2, v3):
    return v1 + v2 + v3

li=[2, 4, 5]
su=sumar(*li)
print(su)


def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


# bloque principal

print("La suma de 1+2")
print(sumar(1,2))
print("La suma de 1+2+3+4")
print(sumar(1,2,3,4))
print("La suma de 1+2+3+4+5+6+7+8+9+10")
print(sumar(1,2,3,4,5,6,7,8,9,10))

"""
Funciones: llamada a la función con argumentos nombrados
"""

def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")                            #end=importante


# bloque principal

lista=cargar()
imprimir(lista)



def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras,"y cobra un sueldo de",sueldo)


# bloque principal

calcular_sueldo("juan",10,120)
calcular_sueldo(costohora=12,cantidadhoras=40,nombre="ana")
calcular_sueldo(cantidadhoras=90,nombre="luis",costohora=7)

"""
Funciones: con parámetros con valor por defecto
"""

def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


# bloque principal

titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Ventas","-")

"""
Funciones: retorno de una lista
"""

def sueldos(persona,sueldo):
    for x in range(10):
        P=input('Nombre:')
        S=float(input('Sueldo:'))
        persona.append(P)
        sueldo.append(S)
    return persona,sueldo

def Sueldomayora4k(persona,sueldo):
    May=[]
    for x in range(len(sueldo)):
        if sueldo[x]>4000:
            May.append(sueldo[x])
    print('Sueldos mayores a 4000')
    print(May)

def debajo_promedio(persona,sueldo,plus):
    print('Personas con sueldo menor al promedio:')
    for x in range(len(sueldo)):
        if sueldo[x]<plus:
            print(persona[x],sueldo[x])

def promedio(persona,sueldo,plus):
    for x in range(len(sueldo)):
        plus=plus+sueldo[x]
    plus=plus/len(sueldo)
    print('el promedio es',plus)
    debajo_promedio(persona,sueldo,plus)



persona=[]
sueldo=[]
sueldos(persona,sueldo)
for x in range(len(persona)):
    print(persona[x],sueldo[x])
Sueldomayora4k(persona,sueldo)
plus=0
promedio(persona,sueldo,plus)


"""
Funciones: parámetros de tipo lista
"""

def mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    print("El valor mayor de la lista es", may)
    print("El valor menor de la lista es", men)


# bloque principal

lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
mayormenor(lista)

"""
Funciones: retorno de datos
"""

def retornar_superficie(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

va=int(input("Ingrese el valor del lado del cuafrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)

"""
Funciones: parámetros
"""

def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


# programa principal

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")

"""
Concepto de funciones - Programación estructurada
"""

def presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")


def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def finalizacion():
    print("*******************************")
    print("Gracias por utilizar este programa")


# programa principal

presentacion()
carga_suma()
finalizacion()

"""
Listas: eliminación de elementos
"""

lista=[]
for x in range(10):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

print(lista)

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1

print(lista)


lista=[10, 20, 30, 40, 50]

print(lista)

lista.pop(0)
lista.pop(1)
lista.pop(2)

print(lista)


"""
Listas: carga por teclado de componentes de tipo lista
"""

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

lista=[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
print(suma)

"""
Listas: ordenamiento con listas paralelas
"""

paises=[]
habitantes=[]
for x in range(5):
    pa=input('Nombre del pais:')
    paises.append(pa)
    ha=int(input('habitantes del pais:'))
    habitantes.append(ha)

for k in range(4):
    for x in range(4-k):
        if habitantes[x]<habitantes[x+1]:
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1
            aux2=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux2

print('Paises y sus habitantes de mayor a menor')
for x in range(len(paises)):
    print('El pais',paises[x],'tiene',habitantes[x],'habitantes')

#Cambio de ejercicio

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
Listas: ordenamiento de sus elementos
"""

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

print("Lista ordenada")
print(sueldos)

"""
Listas paralelas
"""

def suma1(productos,precios):
    producto=input('coloque el producto:')
    for x in range(len(productos)):
        if producto==productos[x]:
            print('el precio de',productos[x],'es:',precios[x])

productos=['manzana','banana','pera','naranja','limon']
precios=[12,11,32,10,43]
seguir1='si'
while seguir1=='si':
    suma1(productos,precios)
    elegir1=input('Quiere seguir (si/no):')
    if elegir1=='si':
        seguir1='si'
    elif elegir1=='no':
        seguir1='no'


"""
Listas: mayor y menor elemento
"""

lista1=[]

for x in range(10):
    num1=int(input('Coloque un numero:'))
    lista1.append(num1)

mayor=lista1[0]
for x in range(len(lista1)):
    if lista1[x]>mayor:
        mayor=lista1[x]

print('Mayor de la lista:',mayor)

menor=lista1[0]
for x in range(len(lista1)):
    if lista1[x]<menor:
        menor=lista1[x]

print('el menor de la lista:',menor)


"""
Listas: carga por teclado de sus elementos
"""

print('.append')

"""
Estructura de datos tipo lista
"""

def Alista(lista):
    for x in range(10):
        num=int(input('Coloque un numero:'))
        lista.append(num)
    return lista

def May100(lista):
    print('Los numeros mayores a 100 son:')
    for x in range(len(lista)):
        if lista[x]>100:
            print(lista[x])

lista=[]
Alista(lista)
May100(lista)

"""
Procesar cadenas de caracteres
"""

print('aca viene len y [0]')
print('upper() : devuelve una cadena de caracteres convertida todos sus caracteres a mayúsculas. lower() : devuelve una cadena de caracteres convertida todos sus caracteres a minúsculas. capitalize() : devuelve una cadena de caracteres convertida a mayúscula solo su primer caracter y todos los demás a minúsculas.')

"""
Variables enteras, flotantes y cadenas de caracteres
"""

print('float, int, input')

"""
comentarios
"""

print('comentarios')

"""
Estructura repetitiva while y for
"""

x=1900
while x<=2020:
    print(x)
    if x==2020:
        for z in range(10):
            print("Coronavirus, COVID-19")
    elif x==2008:
        for z in range(10):
            print('Coronavirus, SARS')
    elif x==2001:
        for z in range(10):
            print('Crisis en Argentina')
    elif x==1983:
        for z in range(10):
            print('Guerra de Malvinas')
    elif x==1945:
        for z in range(10):
            print('Finaliza la 2da guerra Mundial')
    elif x==1939:
        for z in range(10):
            print('Comienza la 2da Guerra Mundial')
    elif x==1918:
        for z in range(10):
            print('Finaliza la 1era Guerra Mundial')
    elif x==1914:
        for z in range(10):
            print('Comienza la 1era Guerra Mundial')
    x=x+1

"""
Condiciones compuestas con operadores lógicos
"""

print("aca va and, or")

"""
Estructuras condicionales anidadas
"""

print("aca va else")

"""
Estructuras condicionales simples y compuestas
"""

print("aca va el if")

"""
Estructura de programación secuencial
"""

def perimetro():
    lado=float(input("Coloque la medida del lado de un cuadrado:"))
    perimetro=lado*4
    print(perimetro)

def sueldo():
    horas=int(input("Coloque la cantidad de horas que trabaja por quincena:"))
    precio=float(input("Coloque el precio al cual se le paga por hora:"))
    sueldo=horas*precio
    print("El sueldo que se le deberia pagar por quincena es:",sueldo)

def opcion():
    opcion=input("Elija si quiere saber su sueldo (sueldo) o el perimetro de un cuadrado (perimetro):")
    if opcion=='sueldo':
        sueldo()
    elif opcion=='perimetro':
        perimetro()

seguir='si'
while seguir=='si':    #la clave del mundo xd
    opcion()
    elegir=input('Quiere seguir (si/no):')
    if elegir=='si':
        seguir='si'
    elif elegir=='no':
        seguir='no'
