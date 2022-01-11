
import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.begin_fill()   #Rellenar
t.circle(-100)
t.circle(100)
t.end_fill()    #terminar de rellenar

t.begin_fill()
t.color("white","white")
t.circle(-50)
t.circle(50)
t.end_fill()

t.shape("turtle")   #Cambiar figuras
t.shape("arrow")
t.shape("circle")
t.shape("square")
t.shape("triangle")
t.shape("classic")

t.penup()   #Para q no dibuje linea
t.fd(100)
t.pendown()
t.fd(100)

t.undo()    #Se regresa y deja de hacer la ultima accion
t.clear()   #Se limpia toda la pantalla, pero la tortuga en el mismo lugar
t.reset()   #El programa se reinicia por completo

t.fd(100)
t.stamp()   #Dejar un sello o marca de agua o una tortuga mas
t.fd(100)



turtle.done()
