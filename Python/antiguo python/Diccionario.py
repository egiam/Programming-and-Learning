
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




#utilizar como clave el nombre de productos y como valor el precio del mismo.
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



#nombres de paises como clave y como valor la cantidad de habitantes.
def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])


paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises)
