x=0
suma = 0
cant = int(input("Ingrese la cantidad de notas evaluadas: "))
prom=float(input("ingrese la nota necesaria para promocionar:"))
while x<cant:
    nota=float(input("Ingrese la nota:"))
    suma=suma+nota
    x=x+1
promedio=suma/cant
print("La suma da")
print(suma)
print("El promedio da")
print(promedio)
if promedio>=prom:
    print("Usted a promocionado")
if promedio<prom:
    print("Usted a suspendido")



x1=0
x2=0
suma=0
suma1=0
while x1<15:
    valor=float(input("colocar un valor para la lista 1:"))
    suma=suma+valor
    x1=x1+1
while x2<15:
    valor1=float(input("colocar un valor para la lista 2:"))
    suma1=suma1+valor1
    x2=x2+1
if suma==suma1:
    print("las listas son iguales")
else:
    if suma>suma1:
        print("la lista 1 es mayor")
    else:
        print("la lista 2 es mayor")
