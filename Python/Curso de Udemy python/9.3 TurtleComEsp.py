
import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) #Aumentar velocidad, del 1 al 10(max)

t.circle(10)    #Graficar circulo, entre parentecis el radio
t.circle(50)
t.speed(10)
t.circle(100)

t.dot(30)   #Punto, (Diametro)

t.hideturtle()  #La tortuga desaparece
t.speed(1)
t.circle(75)
t.showturtle()  #Para q aparezca la tortuga
t.circle(125)

t.setx(100) #Movilizar a la tortuga en el eje x, pero manteniendo el eje y
t.sety(-100)    #Movilizar pero por el eje Y


turtle.done()
