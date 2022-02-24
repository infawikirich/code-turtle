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
turtle.fillcolor('forest green')


def draw_line(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def shoreline(x1, y1, x2, y2, ratio):
    L = dist((x1, y1), (x2, y2))
    if L <= 1:
        draw_line(x1, y1, x2, y2)
        return

    rs = ratio + random.uniform(-0.1, 0.1)   # let ratio fluctuate slightly around the chosen value
    rs = max(0.5, rs)    # make sure ratio stays at least half of the length
    midx = (x1 + x2)/2 # center of ellipse
    midy = (y1 + y2)/2
    rx = L/2 + (2 * rs - 1)/2*L   # width of ellipse
    ry = ((L*rs)**2 - (L/2)**2)**0.5   # height of ellipse
    theta = math.atan2(y2 - y1, x2 - x1)   # the tilt angle of ellipse
    alpha = random.uniform(math.pi*0.3, math.pi*0.7)   # flucuate around math.pi/2
    x3 = rx*math.cos(alpha)*math.cos(theta) - ry*math.sin(alpha)*math.sin(theta) + midx # parmetric equation for ellipse
    y3 = rx*math.cos(alpha)*math.sin(theta) - ry*math.sin(alpha)*math.cos(theta) + midy
    shoreline(x1, y1, x3, y3, ratio)   # do this recursively on each segment
    shoreline(x3, y3, x2, y2, ratio)


turtle.begin_fill()
shoreline(-300, 0, 300, 0, 0.55)   # call recursion
shoreline(300, 0, -300, 0, 0.55)   # call recursion
turtle.end_fill()
turtle.update()


turtle.mainloop()
