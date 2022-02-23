"""
script file: spiral_star.py

Purpose: This program uses turtle to draw a  circle of squares

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


# create a function to draw a square
def star(length_of_sides):
    """This function draws a square"""
    for k in range(5):
        t.fd(length_of_sides)
        t.lt(144)


length_of_sides = 5

for k in range(100):
    star(length_of_sides)
    t.lt(5)
    length_of_sides += 5




t.ht()
turtle.mainloop()
