
"""
Llamada de métodos desde otro método de la misma clase
"""

#ejercicio
class Agenda:

    def __init__(self):
        self.contactos={}

    def menu1(self):
        opcion=0
        while opcion!=5:
            print('1- Carga de un contacto en la agenda.')
            print('2- Listado completo de la agenda.')
            print('3- Consulta ingresando el nombre de la persona.')
            print('4- Modificación de su teléfono y mail.')
            print('5- Finalizar programa.')
            opcion=int(input('Que desea hacer: '))

            if opcion==1:
                self.carga_contacto()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificar()

    def carga_contacto(self):
        nombre=input('Ingrese el nombre del contacto: ')
        tel=int(input('Ingrese el telefono del contacto: '))
        mail=input('Ingrese el mail del contacto: ')
        self.contactos[nombre]=(tel,mail)
        print('____________________________________________________________')

    def listado(self):
        for cant in self.contactos:
            print(cant,self.contactos[cant],sep='/')
        print('____________________________________________________________')


    def consulta(self):
        consilt=input('Nombre del contacto a buscar: ')
        if consilt in self.contactos:
            print(self.contactos[consilt])
        print('____________________________________________________________')


    def modificar(self):
        name=input('contacto a modficar: ')
        if name in self.contactos:
            tel=input('ingrese nuevo telefono: ')
            mail=input('ingrese nuevo mail: ')
            self.contactos[name]=(tel,mail)
        print('____________________________________________________________')


agenda=Agenda()
agenda.menu1()


#Ejemplo2
class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()

    def cargar(self):
        for x in range(5):
            nom=input("Ingrese nombre del alumno:")
            self.nombres.append(nom)
            no=int(input("Nota del alumno:"))
            self.notas.append(no)

    def listar(self):
        print("Listado completo de alumnos")
        for x in range(5):
            print(self.nombres[x],self.notas[x])
        print("_____________________")

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for x in range(5):
            if self.notas[x]>=7:
                print(self.nombres[x],self.notas[x])
        print("_____________________")


alumnos=Alumnos()
alumnos.menu()

#Ejemplo1
class Operacion1:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La rersta es",resta)

    def multiplicar(self):
        multi=self.valor1*self.valor2
        print("El producto es",multi)

    def dividir(self):
        divi=self.valor1/self.valor2
        print("La division es",divi)


operacion1=Operacion1()

"""
Método __init__ de la clase
"""

#ejercicio2
from math import pow
class Operaciones:

    def __init__(self):
        self.Val1=int(input("Colocar un numero: "))
        self.Val2=int(input("Colocar otro numero: "))

    def operacionando(self):
        V1=self.Val1
        V2=self.Val2
        suma=V1+V2
        resta=V1-V2
        mult=V1*V2
        div=V1//V2
        exp=pow(V1,V2)
        print('su suma es: ',suma)
        print('su resta es: ',resta)
        print('su multiplicacion es: ',mult)
        print('su divicion es: ',div)
        print('su exponenciacion es: ',exp)


operaciones=Operaciones()
operaciones.operacionando()


#ejercicio1
class Cuadrado:

    def __init__(self):
        self.lado=float(input('Lado del cuadrado: '))

    def perimetro_superficie(self):
        x=self.lado*4
        z=self.lado*2
        print('su perimetro es: ',x)
        print('su superficie es: ',z)

cuadrado=Cuadrado()
cuadrado.perimetro_superficie()

#Ejemplo2
class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def imprimir(self):
        print("Coordenada del punto")
        print("(",self.x,",",self.y,")")

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrante")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")


punto1=Punto(10,-2)
punto1.imprimir()
punto1.imprimir_cuadrante()


#Ejemplo1
class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")


empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

"""
Declaración de una clase y creación de objetos
"""

#ejercicio2
class triangulo:

    def inicializar(self,lados):
        self.lados=lados

    def lado_mayor(self):
        y=self.lados[0]
        x=self.lados[1]
        z=self.lados[2]
        print('El valor del lado mayor es:')
        if x<z and z>y:
            print(z)
        elif x<y and y>z:
            print(y)
        else:
            print(x)

    def equilatero(self):
        y=self.lados[0]
        x=self.lados[1]
        z=self.lados[2]
        if y==x and y==z:
            print('El triangulo es equilatero')

triangulo001=triangulo()
lados=[]
for x in range(3):
    Lad=float(input('Lado del triangulo: '))
    lados.append(Lad)

triangulo001.inicializar(lados)
triangulo001.lado_mayor()
triangulo001.equilatero()


#ejercicio1
class persona001:

    def inicializar(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def visualizacion(self):
        print('Datos: ',self.nombre,self.edad)

    def mayor_18(self):
        if self.edad>=18:
            print(self.nombre,'es mayor de edad')
        else:
            print(self.nombre,'es menor de edad')

persona01=persona001()
Name=input('Coloque el nombre: ')
Age=int(input('Coloque su edad: '))
persona01.inicializar(Name,Age)
persona01.visualizacion()
persona01.mayor_18()



saber=input('Quiere saber sobre los objetos(definicion) [s/n]: ')
if saber=='s':
    print('La programación orientada a objetos se basa en la definición de clases; a diferencia de la programación estructurada, que está centrada en las funciones.')
    print('Una clase es un molde del que luego se pueden crear múltiples objetos, con similares características.')
    print('Un poco más abajo se define una clase Persona y luego se crean dos objetos de dicha clase.')
    print('Una clase es una plantilla (molde), que define atributos (lo que conocemos como variables) y métodos (lo que conocemos como funciones).')
    print('La clase define los atributos y métodos comunes a los objetos de ese tipo, pero luego, cada objeto tendrá sus propios valores y compartirán las mismas funciones.')
    print('Debemos declarar una clase antes de poder crear objetos (instancias) de esa clase. Al crear un objeto de una clase, se dice que se crea una instancia de la clase o un objeto propiamente dicho.')

#Ejemplo2
class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


alumno1=Alumno()
alumno1.inicializar("diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()


#Ejemplo1
class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)


persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()
