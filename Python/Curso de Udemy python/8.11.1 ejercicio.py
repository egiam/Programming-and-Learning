
class Universidad():
    def Nombre(self,nombre):
        self.nombre = nombre

class Carrera(Universidad):
    def carrera(self,especialidad):
        self.especialidad = especialidad

class Estudiante(Carrera):
    def datos(self,name,edad):
        self.name = name
        self.edad = edad
        print("Mi nombre es {}, tengo {}, mi especialidad es {}. Estudio en la universidad {}".format(self.name,self.edad,self.especialidad,self.nombre))

persona = Estudiante()
persona.Nombre("UTN")
persona.carrera("Programacion")
persona.datos("Ezequiel",18)
