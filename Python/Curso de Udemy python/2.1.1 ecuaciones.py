
#formula de resolucion de ecuaciones

from math import sqrt

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

x1 = 0
x2 = 0

if ((b**2)-(4*a*c)) < 0:
    print("No se puede resolver por ser numero negativo")
else:
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)

print("x1 es: ",x1,", x2 es: ",x2)
