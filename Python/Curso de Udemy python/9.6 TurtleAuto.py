import turtle

s = turtle.Screen()
t = turtle.Turtle()

for x in range(4):
    t.fd(100)
    t.rt(90)


t.speed(10)
x = 200
while x >= 10:
    t.circle(x)
    x = x-10



turtle.done()
