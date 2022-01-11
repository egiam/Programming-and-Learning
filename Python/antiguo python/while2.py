print("Para calcular las notas mayores o iguales a 7")
conti1=int(input("si quiere continuar presione 1 sino quiere presione 2:"))
if conti1==1:
    x=0
    notas=0
    while x<10:
        nota=float(input("ingrese nota:"))
        if nota>=7:
            notas=notas+1
        x=x+1
    print("la cantidad de notas mayores o iguales a 7 son")
    print(notas)
    print("Para calcular altura general")
    conti2=int(input("si quiere continuar presione 1 sino quiere presione 2:"))
    if conti2==1:
        x=0
        suma=0
        n=int(input("ingrese la cantidad de personas:"))
        while x<n:
            altura=float(input("ingrese la altura:"))
            suma=suma+altura
            x=x+1
        promedio=suma/n
        print("la altura promedio es")
        print(promedio)
        print("Para sueldos de empleados")
        continuar=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
        if continuar==1:
            x=0
            cantidad1=0
            cantidad2=0
            suma=0
            n=int(input("ingrese la cantidad de empleados:"))
            while x<n:
                sueldo=int(input("ingrese el sueldo:"))
                if sueldo<=300 and sueldo>=100:
                    cantidad1=cantidad1+1
                if sueldo>300:
                    cantidad2=cantidad2+1
                suma=suma+sueldo
                x=x+1
            print("La cantidad de empleados que cobran entre 100 y 300 son")
            print(cantidad1)
            print("La cantidad de empleados que cobran mas de 300 son")
            print(cantidad2)
            print("El importe gastado por la empresa en sueldos es")
            print(suma)
            print("Para colocar valor de 2 listas")
            conti3=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
            if conti3==1:
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
        if continuar==2:
            print("Para colocar valor de 2 listas")
            conti3=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
            if conti3==1:
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
    if conti2==2:
        print("Para sueldos de empleados")
        continuar=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
        if continuar==1:
            x=0
            cantidad1=0
            cantidad2=0
            suma=0
            n=int(input("ingrese la cantidad de empleados:"))
            while x<n:
                sueldo=int(input("ingrese el sueldo:"))
                if sueldo<=300 and sueldo>=100:
                    cantidad1=cantidad1+1
                if sueldo>300:
                    cantidad2=cantidad2+1
                suma=suma+sueldo
                x=x+1
            print("La cantidad de empleados que cobran entre 100 y 300 son")
            print(cantidad1)
            print("La cantidad de empleados que cobran mas de 300 son")
            print(cantidad2)
            print("El importe gastado por la empresa en sueldos es")
            print(suma)
        if continuar==2:
            print("Para colocar valor de 2 listas")
            conti3=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
            if conti3==1:
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
if conti1==2:
    print("Para calcular altura general")
    conti2=int(input("si quiere continuar presione 1 sino quiere presione 2:"))
    if conti2==1:
        x=0
        suma=0
        n=int(input("ingrese la cantidad de personas:"))
        while x<n:
            altura=float(input("ingrese la altura:"))
            suma=suma+altura
            x=x+1
        promedio=suma/n
        print("la altura promedio es")
        print(promedio)
        print("Para sueldos de empleados")
        continuar=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
        if continuar==1:
            x=0
            cantidad1=0
            cantidad2=0
            suma=0
            n=int(input("ingrese la cantidad de empleados:"))
            while x<n:
                sueldo=int(input("ingrese el sueldo:"))
                if sueldo<=300 and sueldo>=100:
                    cantidad1=cantidad1+1
                if sueldo>300:
                    cantidad2=cantidad2+1
                suma=suma+sueldo
                x=x+1
            print("La cantidad de empleados que cobran entre 100 y 300 son")
            print(cantidad1)
            print("La cantidad de empleados que cobran mas de 300 son")
            print(cantidad2)
            print("El importe gastado por la empresa en sueldos es")
            print(suma)
            print("Para colocar valor de 2 listas")
            conti3=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
            if conti3==1:
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
    if conti2==2:
        print("Para sueldos de empleados")
        continuar=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
        if continuar==1:
            x=0
            cantidad1=0
            cantidad2=0
            suma=0
            n=int(input("ingrese la cantidad de empleados:"))
            while x<n:
                sueldo=int(input("ingrese el sueldo:"))
                if sueldo<=300 and sueldo>=100:
                    cantidad1=cantidad1+1
                if sueldo>300:
                    cantidad2=cantidad2+1
                suma=suma+sueldo
                x=x+1
            print("La cantidad de empleados que cobran entre 100 y 300 son")
            print(cantidad1)
            print("La cantidad de empleados que cobran mas de 300 son")
            print(cantidad2)
            print("El importe gastado por la empresa en sueldos es")
            print(suma)
            print("Para colocar valor de 2 listas")
            conti3=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
            if conti3==1:
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
        if continuar==2:
            print("Para colocar valor de 2 listas")
            conti3=int(input("si quiere continuar presione 1 si no quiere presione 2:"))
            if conti3==1:
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
