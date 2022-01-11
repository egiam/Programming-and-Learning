num1=int(input("coloque un numero:"))
num2=int(input("coloque otro numero:"))
num3=int(input("coloque otro numero:"))
print("el mayor de los 3 es")
if num1>num3 and num1>num2:
    print(num1)
if num2>num3 and num2>num1:
    print(num2)
else:
    print(num3)
