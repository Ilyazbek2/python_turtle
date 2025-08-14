import turtle as t
import random

colors = ["red", "orange", "yellow", "green", "blue"]

def hexagon(side):
    t.begin_fill()
    for _ in range(6):
        t.forward(side)
        t.left(60)
    t.end_fill()

t.speed(0)
t.penup()
t.goto(-200, 200)
t.pendown()

side = 40
rows = 5
cols = 5

for row in range(rows):
    for col in range(cols):
        t.color(random.choice(colors))
        hexagon(side)
        t.penup()
        t.forward(side * 2)
        t.pendown()
    t.penup()
    t.backward(side * 2 * cols)
    t.right(60)
    t.forward(side)
    t.left(60)
    if row % 2 == 0:
        t.forward(side)
    else:
        t.backward(side)
    t.pendown()

t.hideturtle()
t.done()
