import turtle as t
import random

colors = ["red", "orange", "yellow", "green", "blue"]

t.speed(0)
t.bgcolor("black")

for i in range(72):
    t.color(random.choice(colors))
    t.circle(100)
    t.right(5)

t.hideturtle()
t.done()
