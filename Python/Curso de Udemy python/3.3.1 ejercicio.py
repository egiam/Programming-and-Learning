
#valor absoluto

numero = int(input("coloque un numero: "))

if numero < 0:
    x = numero*-1
    print(x)
else:
    x = numero
    print(x)


#letra vocal o no

letra = input("coloque una letra por favor: ")

if letra in "aeiou":
    print("la letra colocada es vocal")
else:
    print("la letra colocada no es vocal")
