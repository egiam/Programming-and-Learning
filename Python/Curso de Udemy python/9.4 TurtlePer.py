import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red")
s.title("Proyecto1.1")  #Cambiar el nombre de la pestania

t.shapesize(10, 5, 1)   #Tamanio de la tortuga, (Ancho, Largo, El borde)
t.shapesize(5,10,1)
t.shapesize(3,3,3)

t.pensize(5)    #Tamanio de linea

t.fillcolor("blue") #Color de la tortuga
t.pencolor("white") #Color del borde
t.fd(100)
t.color("white","blue") #Color de linea y la tortuga
t.rt(90)
t.fd(100)


turtle.done()
