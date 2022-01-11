
while True:
    try:
        edad = int(input("Coloque su edad: "))
        print("Su edad es: ",edad)
        break
    except ValueError:
        print("Ha colocado el valor erroneo")
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecucion")
        break


while True:
    try:
        num1 = int(input("Ingresa un numero: "))
        resultado = 100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("Coloque un numero por favor, no una palabra... idiota.")


while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: {}".format(edad))
        break
    except:
        print("Ingresaste un valor erroneo, intenta nuevamente.")
    finally:
        #para finalizar
        print("La ejecucion a finalizado")
