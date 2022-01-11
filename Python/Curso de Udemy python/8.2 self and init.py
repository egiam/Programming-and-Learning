
class Persona():
    nombre = False

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        print("has creado el objeto persona. Con el nombre {} y el apellido {}".format(nombre,apellido))

    def datos(self):
        self.nombre = True


persona = Persona("Juan", "Carranza")
persona.datos()
print(persona.nombre)
