import turtle

def draw_star():
    side = int(input("Введите длину стороны звезды: "))
    t = turtle.Turtle()
    t.color("blue")
    t.width(2)

    for i in range(5):
        t.forward(side)
        t.right(144)

    turtle.done()

draw_star()