
def agregar_numeros():
    i = 0
    while i < 5:
        num = int(input("coloque un numero: "))
        i += 1
        lista.append(num)

def par_impar(lista,ls_par,ls_impar):
    lista.sort()
    for i in lista:
        if i%2 == 0:
            ls_par.append(i)
        else:
            ls_impar.append(i)
    print("la lista par es: ",ls_par)
    print("la lista impar es: ",ls_impar)


lista = [24,23,22,21]

print(lista)

agregar_numeros()

print(lista)

ls_par = []
ls_impar = []

par_impar(lista,ls_par,ls_impar)
