import turtle

t = turtle.Turtle()
t.speed(0)

#turtle.numinput(title, prompt, default=None, minval=None, maxval=None)
nivel = turtle.numinput("Floco de Kotch", "Digite a quantidade de nivel de recursão desejado")


t.penup()
#goto(x, y)
t.goto(-200, 120)
t.pendown()


def koch(t, tamanho, nivel):
    if nivel == 0:
        t.forward(tamanho)
    else:
        tamanho = tamanho/3

        koch(t, tamanho, nivel- 1)
        t.left(60)

        koch(t, tamanho, nivel- 1)
        t.right(120)

        koch(t, tamanho, nivel- 1)
        t.left(60)

        koch(t, tamanho, nivel- 1)


def floco_de_koch(t, tamanho, nivel):
    for i in range(3):
        koch(t, tamanho, nivel)
        t.right(120)



floco_de_koch(t, 400, nivel)


turtle.done() #não deixa que a aplicação feche!