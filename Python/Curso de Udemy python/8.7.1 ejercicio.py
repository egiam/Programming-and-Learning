
class Alumn():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno {} tiene una nota de {}".format(self.nombre,self.nota))

    def aprove(self):
        if self.nota > 6:
            print("El alumno {} ha aprovado".format(self.nombre))
        else:
            print("El alumno {} no ha aprovado".format(self.nombre))


nombre = input("Coloque el nombre del alumno: ")
nota = int(input("Coloque la nota del alumno: "))
alumn = Alumn(nombre,nota)
alumn.aprove()
