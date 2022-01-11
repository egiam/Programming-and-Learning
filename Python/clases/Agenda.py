
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
