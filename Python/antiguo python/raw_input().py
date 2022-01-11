

#prueba de len
oracion=raw_input("coloque una oracion de no mas de 50 letras:")
if len(oracion)<=50:
    n=int(input("coloque el numero entero que quiera de mas de 10 caracteres:"))
    if n>=10:
        x=1
        while x<=n:
            print(x)
            x=x+1

#oracion para contar vocales
oracion=raw_input("Ingrese una oracion:")
oracionmin=oracion.lower()
cantidad=0
x=0
while x<len(oracionmin):
    if oracionmin[x]=="a" or oracionmin[x]=="e" or oracionmin[x]=="i" or oracionmin[x]=="o" or oracionmin[x]=="u":
        cantidad=cantidad+1
    x=x+1
print("La cantidad de vocales de la oracion son")
print(cantidad)


#clave almacenada
clave=raw_input("ingrese clave de mas de 10 caracteres pero menos de 20:")
if len(clave)<=20 and len(clave)>=10:
    print"la clave ha sido guardada con exito"
else:
    print"la clave no cumple con los requisitos, intente de nuevo."
    clave=raw_input("ingrese clave de mas de 10 caracteres pero menos de 20:")
    if clave<20 and clave>10:
        print"la clave ha sido guardada con exito"
if clave<10 or clave>20:
        print"la clave no cumple con los requisitos, intente de nuevo."



#espacios en blanco
blanco=raw_input("escriba lo que se le cante:")
cantidad=0
x=0
while x<len(blanco):
    if blanco[x]==" ":
        cantidad=cantidad+1
    x=x+1
print("la cantidad de espacios en blanco es")
print(cantidad)


nombre1="mAriA"
print(nombre1)
nombre2=nombre1.upper()
print(nombre2)
nombre3=nombre1.lower()
print(nombre3)
nombre4=nombre1.capitalize()
print(nombre4)

mail=raw_input("Ingrese un mail:")
cantidad=0
x=0
while x<len(mail):
    if mail[x]=="@":
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")

#problema de alfabetismo en nombres
nombre1=raw_input("coloque un nombre:")
print("primer caracter")
print(nombre1[0])
print("cantidad de letras del nombre")
print(len(nombre1))
nombre2=raw_input("coloque otro nombre:")
print("primer caracter")
print(nombre2[0])
print("cantidad de letras del nombre")
print(len(nombre2))
print("el orden alfabetico de los nombres es")
if nombre1<nombre2:
    print(nombre1)
    print(nombre2)
else:
    print(nombre2)
    print(nombre1)


#pendejadas
print"cual es tu nombre?"
nombre=raw_input()
print"hola "+nombre
print"te gusta vivir aqui?"
vivir=raw_input()
if nombre=="eze" and vivir=="si":
    print("te amo")


#otra pendejada
opcion1="si"
suma=0
while opcion1=="si":
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    opcion=raw_input("Desea cargar otro numero (si/no):")
    opcion1=opcion.lower()
print("La suma de valores ingresados es")
print(suma)
