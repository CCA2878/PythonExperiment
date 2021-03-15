import turtle
from random import *
turtle1 = turtle
turtle1.setup(400,300,50,50)
turtle1.colormode(255)
turtle1.speed(1)
i = 40
while i >= 1:
    turtle1.pensize(i)
    turtle1.pencolor((randint(0,255),randint(0,255),randint(0,255)))
    turtle1.fd(100)
    turtle1.lt(90)
    i += -4

input()