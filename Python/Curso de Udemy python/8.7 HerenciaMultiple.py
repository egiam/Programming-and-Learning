
class A():
    def mensaje(self):
        print("esta es la clase A")

    def primera(self):
        print("estas dentro de la clase A")

class B():
    def mensaje(self):
        print("esta es la clase B")

    def segunda(self):
        print("estas dentro de la clase B")

class C(A,B): #el mas a la izquierda es la primera dependencia
    pass

c = C()
c.mensaje()
c.primera()
c.segunda()
