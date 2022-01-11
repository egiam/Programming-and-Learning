conti=input("calcular precio de pan, si quiere calcularlo presione 1 si no quiere presione 2:")
if conti==1:
    precio=0.06
    cantidad=float(input("coloque la cantidad de kilogrammos de pan a comprar:"))
    total=precio*cantidad
    print("precio por kilo")
    print(precio)
    print("precio total a pagar")
    print(total)
    cont1=input("calculadora de prueba, si quiere probarlo presione 1 si no quiere presione 2:")
    if cont1==1:
        x=0
        while x<10:
            num1=float(input("numero:"))
            num2=float(input("numero:"))
            suma=num1+num2
            multiplicacion=num1*num2
            resta=num1-num2
            divicion=num1/num2
            potencia=num1**num2
            opcion=input("si quiere sumar presione 1, si quiere multiplicar presione 2, si quiere restar presione 3, si quiere dividir presione 4, si quiere potenciar presione 5:")
            if opcion==1:
                print(suma)
            else:
                if opcion==2:
                    print(multiplicacion)
                else:
                    if opcion==3:
                        print(resta)
                    else:
                        if opcion==4:
                            print(divicion)
                        else:
                            print(potencia)
