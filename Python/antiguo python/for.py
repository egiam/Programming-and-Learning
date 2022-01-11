n=int(input("cantidad de triangulos:"))
for x in range(n):
    lado1=float(input("1er lado de triangulo:"))
    lado2=float(input("2do lado de triangulo:"))
    lado3=float(input("3er lado de triangulo:"))
    if lado1==lado2 and lado1==lado3:
        print("el triangulo es equilatero")
    if lado2<lado3 or lado2>lado3 and lado2==lado1 or lado2<lado1 or lado2>lado1 and lado2==lado3:
        print("el triangulo es isosceles")
    if lado3<lado2 or lado3>lado2 and lado3<lado1 or lado3>lado1:
        print("el triangulo es escaleno")


for x in range(1,100,2):
    print(x)

suma=0
for x in range(10):
    valor=int(input("valor:"))
    suma=suma+valor
promedio=suma/10
print("el promedio es")
print(promedio)

suma=-5
for x in range(10):
    numeros=float(input("numero:"))
    suma=suma
