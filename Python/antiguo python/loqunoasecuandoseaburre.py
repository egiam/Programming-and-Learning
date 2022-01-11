
"""
Abecedario
"""

print('Abecedario')
ABC=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for x in range(len(ABC)):
    print('*')
    print(ABC[x])


"""
Calcular el numero promedio total
"""

def promedio1(lista):
    total=0
    for x in range(len(lista)):
        total=total+lista[x]
    promedio=total/len(lista)
    print('El promedio de los numeros es:',promedio)

    return promedio

def numeros(lista):
    C=int(input('Cantidad de numeros a colocar: '))
    z=1
    for x in range(C):
        Num=float(input('Numero:'))
        z=z+1
        lista.append(Num)

    return lista

lista=[]
numeros(lista)
promedio1(lista)


"""
Calcular total que te queda segun tus ganancias e impuestos por pagar
"""

def impuestos(imp,ganancia):
    total=ganancia[0]*imp[0]
    total=ganancia[0]-total
    print('El dinero total que te queda luego de pagar los impuestos es',total)

def que_tiene(imp,ganancia):
    z=float(input("Coloque su ganancia mensual: "))
    ganancia.append(z)
    t=0
    x=int(input("Coloque la cantidad de impuestos que tiene que pagar a fin de mes: "))
    for k in range(x):
        x1=float(input("coloque el porcentaje que se le quita de cierto impuesto: "))
        t=t+x1
    t=t/100
    imp.append(t)
    return ganancia,imp

ganancia=[]
imp=[]
que_tiene(imp,ganancia)
impuestos(imp,ganancia)
