import turtle
import math

t = turtle.Turtle()
t.speed(0)

def koch(t, tamanho, nivel):
    if nivel == 0:
        t.forward(tamanho)
    else:
        tamanho /= 3

        koch(t, tamanho, nivel - 1)
        t.left(60)

        koch(t, tamanho, nivel - 1)
        t.right(120)

        koch(t, tamanho, nivel - 1)
        t.left(60)

        koch(t, tamanho, nivel - 1)


def floco_de_koch(t, tamanho, nivel):
    for i in range(3):
        koch(t, tamanho, nivel)
        t.right(120)


t.penup()
t.goto(-200, 120)
t.pendown()

floco_de_koch(t, 400, 3)

turtle.done()