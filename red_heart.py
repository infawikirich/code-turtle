"""
script file: red_heart.py

Purpose: This program uses turtle module to draw a rec heart

Author: Mr. Asiamah

Date : 03/04/21

"""

import turtle


# instantiate the turtle module
t = turtle.getturtle()

# instatiate the screen
win = turtle.Screen()
win.setup(800, 600)
win.title('Red Heart')
win.bgcolor('black')

t.speed(0)
t.color('red')
t.ht()

def curve():
    for k in range(200):
        t.fd(1)
        t.rt(1)


t.begin_fill()
t.seth(140)
t.fd(111)
curve()

t.seth(60)
curve()
t.fd(115)

t.end_fill()

turtle.done()