
"""
Redefinición de los operadores relacionales con objetos
"""

#Ejemplo2
class Rectangulo:

    def __init__(self,lmenor,lmayor):
        self.lmenor=lmenor
        self.lmayor=lmayor

    def retornar_superficie(self):
        return self.lmenor*self.lmayor

    def __eq__(self,objeto2):
        if self.retornar_superficie()==objeto2.retornar_superficie():
            return True
        else:
            return False

    def __ne__(self,objeto2):
        if self.retornar_superficie()!=objeto2.retornar_superficie():
            return True
        else:
            return False

    def __gt__(self,objeto2):
        if self.retornar_superficie()>objeto2.retornar_superficie():
            return True
        else:
            return False

    def __ge__(self,objeto2):
        if self.retornar_superficie()>=objeto2.retornar_superficie():
            return True
        else:
            return False

    def __lt__(self,objeto2):
        if self.retornar_superficie()<objeto2.retornar_superficie():
            return True
        else:
            return False

    def __le__(self,objeto2):
        if self.retornar_superficie()<=objeto2.retornar_superficie():
            return True
        else:
            return False


rectangulo1=Rectangulo(10,10)
rectangulo2=Rectangulo(5,20)
if rectangulo1==rectangulo2:
    print("Los rectangulos tienen la misma superficie")
else:
    print("Los rectangulos no tienen la misma superficie")

#Ejemplo1
class Persona:

    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def __eq__(self,objeto2):
        if self.edad==objeto2.edad:
            return True
        else:
            return False

    def __ne__(self,objeto2):
        if self.edad!=objeto2.edad:
            return True
        else:
            return False

    def __gt__(self,objeto2):
        if self.edad>objeto2.edad:
            return True
        else:
            return False

    def __ge__(self,objeto2):
        if self.edad>=objeto2.edad:
            return True
        else:
            return False

    def __lt__(self,objeto2):
        if self.edad<objeto2.edad:
            return True
        else:
            return False

    def __le__(self,objeto2):
        if self.edad<=objeto2.edad:
            return True
        else:
            return False


persona1=Persona('juan',22)
persona2=Persona('ana',22)
if persona1==persona2:
    print("Las dos personas tienen la misma edad.")
else:
    print("No tienen la misma edad.")
