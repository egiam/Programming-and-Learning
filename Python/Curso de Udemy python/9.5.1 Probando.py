import turtle

s = turtle.Screen()
t = turtle.Turtle()

lista = ["turtle","arrow","circle","square","triangle","classic"]

s.bgcolor("red")

for i in lista:
    t.shape(i)
    t.color("black","white")
    t.begin_fill()
    t.circle(-100)
    t.circle(100)
    t.end_fill()
    t.color("white","black")
    t.begin_fill()
    t.circle(-50)
    t.circle(50)
    t.end_fill()


turtle.done()
