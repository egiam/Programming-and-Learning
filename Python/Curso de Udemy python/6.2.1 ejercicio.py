
def numeros():
    num1 = int(input("coloque un numero: "))
    num2 = int(input("coloque otro numero: "))
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

print(numeros())
