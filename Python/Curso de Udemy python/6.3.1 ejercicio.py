
def area_cuadrado(base,altura):
    return base*altura

def area_circulo(radio):
    return (radio**2)*3.14

x = input("quiere medir el area de un cuadrado o un circulo [Cu/Ci]: ")
x.capitalize()

if x == "Cu":
    B = float(input("coloque la base del cuadrado: "))
    A = float(input("coloque la altura del cuadrado: "))
    print("el area del cuadrado es: ",area_cuadrado(B,A))
elif x == "Ci":
    R = float(input("coloque el radio del circulo: "))
    print("el area del circulo es: ",area_circulo(R))
else:
    print("por favor coloque correctamente lo que quiere hacer.")
