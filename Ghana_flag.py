"""
script file: Ghana_flag.py

Purpose: This program uses turtle to draw Ghana Flag
Author: Mr. Asiamah

Date : 02/06/21

"""
import turtle
from turtle import *

win = turtle.Screen()
win.setup(800, 720)
win.bgpic('football_park.png')
win.bgcolor('#123')

win.tracer(0, 0)
speed(0)

def star():
    """This function draws a black star"""
    up()
    goto(65, 170)
    color('#000')

    down()

    begin_fill()

    for k in range(5):
        fd(70)
        rt(144)

    end_fill()


def pole():
    """This function draws the pole of the flag"""

    color("#caa472")
    pu()
    goto(-100, -350)

    down()
    begin_fill()
    for k in range(2):
        fd(30)
        lt(90)
        fd(700)
        lt(90)

    end_fill()


# lift the pen up to draw the cloth part
up()
goto(-70, 0)
down()

def flag(height_flag):
    """This function draws the cloth of the flag with different colors"""

    colors = ['red', 'yellow', 'green']
    colors.reverse()

    for i in range(3):
        color(colors[i])

        goto(-70, i * height_flag)


        begin_fill()

        for k in range(2):
            fd(350)
            lt(90)
            fd(height_flag)
            lt(90)

        end_fill()

        seth(0)


flag(110)
star()
pole()


ht()
win.update()
mainloop()
