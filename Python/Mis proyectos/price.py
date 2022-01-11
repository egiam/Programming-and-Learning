
def seguir_1():
    q=int(input("Coloque la cantidad de cupckakes que quieres comprar: "))
    p=2*q+5
    print("El precio a pagar mas el envio es:",p)

def seguir_2():
    p=int(input("Coloque el precio que pago: "))
    Q=(p-5)/2
    print("Cupckakes a recibir:",Q)

x=1

while x!=0:
    seguir=int(input("-Si quiere comprar x cantidad de cupckakes, presione 1.\n
    -Si quiere averiguar la cantidad de cupckakes en cierto precio, presione 2.\n
    -Si quiere salir del programa, presione 0.\nPresione: "))

    if seguir==1:
        seguir_1()

    if seguir==2:
        seguir_2()

    if seguir==0:
        x=0
