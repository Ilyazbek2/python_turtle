import turtle as t

t.width(5)
t.speed(0)

colors = ["blue", "black", "red", "yellow", "green"]
positions = [(-120, 0), (0, 0), (120, 0), (-60, -50), (60, -50)]

for color, pos in zip(colors, positions):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.pencolor(color)
    t.circle(50)

t.hideturtle()
t.done()
