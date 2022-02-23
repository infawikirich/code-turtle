"""
script file: polygon.py

Purpose: This program uses turtle to draw a polygon of any size

Author: Mr. Asiamah

Date : 01/09/21

"""

import turtle

t = turtle.Turtle()

win = turtle.Screen()
win.setup(800, 540)
win.title("Circle of Square")
win.bgcolor("lightgreen")



t.speed(0)
t.shape('turtle')


def polygon(number_of_sides = 3):
    """This function draws the a polygon"""

    for k in range(number_of_sides):
        t.fd(150)
        t.lt(360/number_of_sides)


number_of_sides = turtle.numinput("Polygon sides", "Enter the sides of the polygon")

polygon(int(number_of_sides))

t.ht()
turtle.mainloop()
