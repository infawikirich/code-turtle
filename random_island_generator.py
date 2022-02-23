import turtle
import math
import random


win = turtle.Screen()
win.setup(1000, 1000)
win.title("Random Island Generator")
win.bgcolor("royal blue")
turtle.pencolor('green')


turtle.speed(0)
turtle.tracer(0, 0)
turtle.hideturtle()


def draw_line(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**2

def shoreline(x1, y1, x2, y2, ratio):
    L = dist((x1, y1), (x2, y2))
    if L <= 1:
        draw_line(x1, y1, x2, y2)
        return







turtle.mainloop()
