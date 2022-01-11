"""
Funciones: con cantidad variable de parámetros
"""

# función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18

def edades():
    edades=int(input("cantidad de edades a colocar: "))
    li=[]
    for x in range(edades):
        ed=int(input("edad del sujeto: "))
        li.append(ed)
    return li

def mayor_edad(lista):
    mayor=0
    for x in range(len(lista)):
        if lista[x]>=18:
            mayor=mayor+1
    return mayor


# bloque principal

lista=edades()
mayor=mayor_edad(lista)
print("cantidad de personas mayores: ", mayor)



# función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros, retornar la suma de dichos parámetros.

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

#tabla de multiplicar de cierto valor
def tabla_mult(v1,v2):
    tabla=[]
    sum=0
    for x in range(v2):
        sum=sum+1
        mult=v1*sum
        tabla.append(mult)
    print("la tabla de multiplicar de ese numero es",tabla)

v1=int(input("valor numerico:"))
v2=10
tabla_mult(v1,v2)

#otra forma
def tabla(numero, terminos=10):
    for x in range(terminos):
        va=x*numero
        print(va,",",sep="",end="")
    print()


# bloque principal

print("Tabla del 3")
tabla(3)
print("Tabla del 3 con 5 terminos")
tabla(3,5)
print("Tabla del 3 con 20 terminos")
tabla(terminos=20,numero=3)



#pago, horas, nombre
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

#función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.
def enteros(caracter="*"):
    v1=int(input("coloque un valor: "))
    print(caracter*25)
    v2=int(input("coloque un valor: "))
    print(caracter*25)
    v3=int(input("coloque un valor: "))
    print(caracter*25)
    v4=int(input("coloque un valor: "))
    print(caracter*25)
    v5=int(input("coloque un valor: "))
    print(caracter*25)
    return [v1,v2,v3,v4,v5]


def suma(valores,caracter="*"):
    suma=0
    for x in range(len(valores)):
        suma=suma+valores[x]
    print(caracter*len(valores))
    print("la suma es",suma)
    print(caracter*len(valores))


valores=enteros("*")
suma=suma(valores,"-")

#otra forma

def sumar(v1,v2,v3=0,v4=0,v5=0):
    s=v1+v2+v3+v4+v5
    return s


# bloque principal

print("La suma de 5 + 6")
print(sumar(5,6))
print("La suma de 1 + 2 + 3")
print(sumar(1,2,3))
print("La suma de 1 + 2 + 3 + 4 + 5")
x=sumar(1,2,3,4,5)
print(x)


#función que reciba un string como parámetro y en forma opcional un segundo string con un caracter.
def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


# bloque principal

titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Ventas","-")


"""
Funciones: retorno de una lista
"""

#10 elementos separados por positivo y negativo
def carga():
    carga=[]
    for x in range(10):
        valor=int(input("numero positivo o negativo:"))
        carga.append(valor)
    return carga


def pos_neg(carga):
    positivo=[]
    negativo=[]
    for x in range(len(carga)):
        if carga[x]>=0:
            positivo.append(carga[x])
        else:
            if carga[x]<0:
                negativo.append(carga[x])
    print("listas de positivo y negativo")
    print(positivo)
    print(negativo)


carga=carga()
pos_neg=pos_neg(carga)


#sueldos de 10 personas. con lista
def sueldos_e():
    sueldos=[]
    for x in range(10):
        S=int(input("ingrese sueldo:"))
        sueldos.append(S)
    print("lista de sueldos",sueldos)
    return sueldos


def superiores(sueldo):
    cant=0
    for x in range(len(sueldo)):
        if sueldo[x]>4000:
            cant=cant+1
    print("cantidad de sueldos mayores a 4000:",cant)
    return cant


def promedio(sueldo):
    suma=0
    for x in range(len(sueldo)):
        suma=suma+sueldo[x]
    promedio=suma//len(sueldo)
    print("el promedio es:",promedio)
    return promedio


def menores_pro(promedio,sueldo):
    print("sueldos menores al promedio")
    for x in range(len(sueldo)):
        if sueldo[x]<promedio:
            print(sueldo[x])


sueldo=sueldos_e()
superior=superiores(sueldo)
promedio=promedio(sueldo)
menpro=menores_pro(promedio,sueldo)



"""
Funciones: parámetros de tipo lista
"""

#lista de enteros multiplicandolos por otro entero
def multiplicado(lista,v1):
    lista1=[]
    for x in range(len(lista)):
        total=lista[x]*v1
        lista1.append(total)
    return lista1


lista=[12,23,21,4,5]
v1=int(input("valor para la multiplicacion:"))
print("el resultado dejado es",multiplicado(lista,v1))

#otra manera
def multiplicar(lista,va):
    for x in range(len(lista)):
        multi=lista[x]*va
        print(multi)


# bloque principal

lista=[3, 7, 8, 10, 2]
print("Lista original:",lista)
print("Lista multiplicando cada elemento por 3")
multiplicar(lista,3)




#una función que reciba la lista y nos retorne el producto de todos sus elementos.
def presentacion():
    print("**********************************************************************************************")
    print("en este proyecto una lista ya dada va a multiplicar todos sus valores dando el resultado final")
    print("**********************************************************************************************")

def producto(lista):
    producto=1
    for x in range(len(lista)):
        producto=producto*lista[x]
    return producto

presentacion()
lista=[3,2,3,2,3]
print("el total es",producto(lista))

#lista de el que tiene más caracteres.
def mascaracteres(palabras):
    pos=0
    for x in range(len(palabras)):
        if len(palabras[x])>len(palabras[pos]):
            pos=x
    return palabras[pos]


# bloque principal

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))

#5 enteros. Implementar una función que imprima el mayor y el menor valor de la lista.
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

#lista con suma, mayor y menor
def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may


def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men


# bloque principal del programa

listavalores=[10, 56, 23, 120, 94]
print("La lista completa es")
print(listavalores)
print("La suma de todos su elementos es", sumarizar(listavalores))
print("El mayor valor de la lista es", mayor(listavalores))
print("El menor valor de la lista es", menor(listavalores))

"""
Funciones: retorno de datos
"""

#contar cantidad de "a"
def cantidad(oracion):
    cantidad=0
    for x in range(len(oracion)):
        if oracion[x]=="a" or oracion[x]=="A":
            cantidad=cantidad+1
    return cantidad

oracion=input("escriba la oracion:")
print("la cantidad de letras a que hay es")
print(cantidad(oracion))

#superficie de rectangulo
def retornar_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie


# bloque principal

print("Primer rectangulo")
lado1=int(input("Ingrese lado menor del rectangulo:"))
lado2=int(input("Ingrese lado mayor del rectangulo:"))
print("Segundo rectangulo")
lado3=int(input("Ingrese lado menor del rectangulo:"))
lado4=int(input("Ingrese lado mayor del rectangulo:"))
if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
    print("Los dos rectangulos tiene la misma superficie")
else:
    if retornar_superficie(lado1,lado2)>retornar_superficie(lado3,lado4):
        print("El primer rectangulo tiene una superficie mayor")
    else:
        print("El segundo rectangulo tiene una superficie mayor")


#perimetro de cuadrado
def perimetro(lado):
    perimetro=lado*4
    return perimetro

lado=float(input("lado del cuadrado:"))
perimetro=perimetro(lado)
print("el perimetro del cuadrado es",perimetro)

#tres enteros y su promedio
def enteros(v1,v2,v3):
    promedio=(v1+v2+v3)/3
    return promedio


val1=float(input("coloque un valor:"))
val2=float(input("coloque un valor:"))
val3=float(input("coloque un valor:"))
promedio=enteros(val1,val2,val3)
print("el promedio es",promedio)

#carga de dos nombres por teclado Imprimir cual de las dos palabras tiene más caracteres.
def largo(cadena):
    return len(cadena)


# bloque principal

nombre1=input("Ingrese primer nombre:")
nombre2=input("Ingrese segundo nombre:")
la1=largo(nombre1)
la2=largo(nombre2)
if la1==la2:
    print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1,"es mas largo")
    else:
        print(nombre2,"es mas largo")

#dos enteros y nos retorne el mayor.
def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor

v1=int(input("ingrese un valor:"))
v2=int(input("ingrese otro valor:"))
mayor=retornar_mayor(v1,v2)
print("el mayor es",mayor)

#valor del lado de un cuadrado y nos retorne su superficie.
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

#tres enteros y los muestre ordenados de menor a mayor.
def ordenar_imprimir(v1,v2,v3):
    if v1<v2 and v1<v3:
        if (v2<v3):
            print(v1,v2,v3)
        else:
            print(v1,v3,v2)
    else:
        if (v2<v3):
            if (v1<v3):
                print(v2,v1,v3)
            else:
                print(v2,v3,v1)
        else:
            if (v1<v2):
                print(v3,v1,v2)
            else:
                print(v3,v2,v1)


def cargar():
    num1=int(input("Ingrese primer valor:"))
    num2=int(input("Ingrese segundo valor:"))
    num3=int(input("Ingrese tercer valor:"))
    ordenar_imprimir(num1,num2,num3)


# bloue principal

cargar()

#cantidad de vocales
def vocales(voc):
    cantidad=0
    for x in range(len(voc)):
        if voc[x]=="a" or voc[x]=="e" or voc[x]=="i" or voc[x]=="o" or voc[x]=="u":
            cantidad=cantidad+1
    print("la cantidad de vocales contenidas en la oracion",voc,"es",cantidad)

#PP
vocales("hola que tal")
vocales("habia una vez trus")
vocales("procariota")

#programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.
def mostrar_perimetro(lado):
    per=lado*4
    print("El perimetro es",per)


def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)


def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?")
    if respuesta=="perimetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)


# programa principal

cargar_dato()


#Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos.
def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)


# programa principal

cargar()

#presentacion, suma, despedida
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
comienzo de funciones
"""

#carga de tres valores y muestre el menor.
def menor_valor():
    valor1=int(input("Ingrese primer valor:"))
    valor2=int(input("Ingrese segundo valor:"))
    valor3=int(input("Ingrese tercer valor:"))
    print("Menor de los tres")
    if valor1<valor2 and valor1<valor3:
        print(valor1)
    else:
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)


# bloque principal

menor_valor()
menor_valor()

#programa con 2 funciones, primera con un valor al cuadrado, segunda con producto de dos valores
def potenciacion():
    num1=int(input("carge un numero para exponenciarlo al cuadrado:"))
    exponente=num1**2
    print("el resultado es:",exponente)
    print("************************************************")

def producto():
    num1=int(input("carge un numero:"))
    num2=int(input("carge otro numero para el producto:"))
    producto=num1*num2
    print("el producto de ambos numeros es:",producto)

#programa principal

potenciacion()
producto()
print("***********************************************")

#aplicacion con dos valores y su suma
def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def separacion():
    print("*******************************")


# programa principal

for x in range(5):
    carga_suma()
    separacion()

#aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma.
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
