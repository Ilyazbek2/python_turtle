import turtle as t
import random

colors = ["red", "orange", "yellow", "green", "blue"]

t.bgcolor("black")
t.speed(0)

t.width(2)

for _ in range(50):
    t.color(random.choice(colors))
    t.forward(200)
    t.right(144)
    t.forward(200)
    t.right(144)
    t.forward(200)
    t.right(144)
    t.forward(200)
    t.right(144)
    t.forward(200)
    t.right(144)
    t.right(10)  # rotate slightly for pattern

t.hideturtle()
t.done()
