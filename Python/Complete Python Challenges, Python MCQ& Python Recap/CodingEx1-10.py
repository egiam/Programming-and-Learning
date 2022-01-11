
#Ejercicio 3





#Ejercicio 2
name1 = input("Coloque su nombre: ");

def empty():
    if name1 == "":
        print("Vacio");
    else:
        print(f"Bienvenido {name1}");

empty();



#Ejercicio 1

name = input("Coloque su nombre: ");

print(f"BIenvenido {name}");

#RTA - No funciona

def hello_there(name):
    return "Hello {}!".format(name)

hello_there('Tamer')
