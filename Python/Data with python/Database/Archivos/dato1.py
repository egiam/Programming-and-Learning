
#Caracteres utf-8

archi1=open("datos.txt","w", encoding="utf-8")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.close()


#Abrir, leer y agregar

archi1=open("datos.txt","r+")
contenido=archi1.read()
print(contenido)
archi1.write("Otra línea 1\n")
archi1.write("Otra línea 2\n")
archi1.close()


#Abrir y añadir

archi1=open("datos.txt","a")
archi1.write("nueva línea 1\n")
archi1.write("nueva línea 2\n")
archi1.close()
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()


#Almacenar archivo en lista

archi1=open("datos.txt","r")
lineas=archi1.readlines()
print('El archivo tiene', len(lineas), 'líneas')
print('El contenido del archivo')
for linea in lineas:
    print(linea, end='')
archi1.close()


#Lectura de linea a linea

#tipo 1

archi1=open("datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea, end='')
    linea=archi1.readline()
archi1.close()

#tipo 2

archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()


#Lectura del archivo

archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()


#Escritura del archibo

archi1=open("datos.txt","w")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.close()
