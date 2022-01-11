import turtle
import random

s = turtle.Screen()

s.title("Primer proyecto")
s.bgcolor("lightgray")


J1 = turtle.Turtle()
J2 = turtle.Turtle()

J1.hideturtle()
J1.shape("turtle")
J1.color("green","green")
J1.shapesize(2,2,2)
J1.pensize(3)

J2.hideturtle()
J2.shape("turtle")
J2.color("blue","blue")
J2.shapesize(2,2,2)
J2.pensize(3)

J1.penup()
J1.goto(250,150)
J1.pendown()
J1.circle(40)

J1.penup()
J1.goto(-250,175)
J1.pendown()

J2.penup()
J2.goto(250,-150)
J2.pendown()
J2.circle(40)

J2.penup()
J2.goto(-250,-125)
J2.pendown()

J1.showturtle()
J2.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if J1.pos() >= (250,150):
        print("La tortuga verde ha ganado. El jugador 1 ha ganado")
        break
    elif J2.pos() >= (250,-150):
        print("La tortuga azul ha ganado. EL jugador 2 ha ganado")
        break
    else:
        turno1 = input("Presiona la tecla enter para avanzar la tortuga verde.")
        turno1 = random.choice(dado)
        print("Tu numero es: ",turno1,"\nAvanzas: ",turno1*20)
        J1.fd(20*turno1)

        turno2 = input("Preciiona la tecla enter para avanzar la tortuga azul.")
        turno2 = random.choice(dado)
        print("Tu numero es: ",turno2,"\nAvanzas: ",turno2*20)
        J2.fd(20*turno2)


turtle.done()
