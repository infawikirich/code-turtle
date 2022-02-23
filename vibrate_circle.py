"""
script file: vibrate_circle.py

Purpose: This program uses turtle module to create a vibrating circle

Author: Mr. Asiamah

Date : 04/03/21

"""

import turtle


# instantiate the turtle module
t = turtle.getturtle()

# instatiate the screen
win = turtle.Screen()
win.setup(800, 600)
win.title('Vibrating Circle')
win.bgcolor('black')

t.color('red')

a, b = 0, 0
t.speed(0)
t.up()
t.goto(0, 200)
t.pd()

while True:
    t.fd(a)
    t.rt(b)

    a += 3
    b += 1

    if b == 210:
        break
    t.ht()

turtle.done()