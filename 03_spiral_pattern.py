import turtle as t
import random

colors = ["red", "orange", "yellow", "green", "blue"]

t.bgcolor("black")
t.speed(0)

for i in range(200):
    t.color(random.choice(colors))
    t.forward(i * 2)
    t.left(59)

t.hideturtle()
t.done()
