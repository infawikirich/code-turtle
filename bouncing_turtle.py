"""
script file: bouncing_turtle.py

Purpose: This program bounces turtle off the edge of the

Author: Mr. Asiamah

Date: 21/07/21

"""

from turtle import *
import turtle, random

win = turtle.Screen()
win.title('Bouncing turtle')
win.bgcolor('lightgreen')

#turtle.tracer(12)
speed(0)
shape('circle')
turtlesize(3, 3, 2)

# lift the turtle pen
up()

while True:

    fd(3)

    if xcor() > window_width()/2 or ycor() > window_height()/2 or xcor() < -window_width()/2 or ycor() < -window_height()/2:
        lt(random.randint(90, 180))





mainloop()



