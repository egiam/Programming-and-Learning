
class Persona():
    nombre = "Carlos"
    apellido = "Vergara"
    sexo = "Masculino"
    edad = 30

    def hablar(self,mensaje):
        return mensaje

persona = Persona()
persona.nombre
persona.apellido
persona.sexo
persona.edad

print(persona.hablar("hola soy"),"{} y mi apellido es {}, tengo {} y soy {}".format(persona.nombre,persona.apellido,persona.edad,persona.sexo))
