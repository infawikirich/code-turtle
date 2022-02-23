"""
 script file: randomWalk.py

 purpose: This program draws a clock using the turtle module

 Author: Mr. Asiamah

 Date: 25/05/21
"""

from turtle import *

speed(0)


def thick():
    pd()
    width(3)
    forward(20)
    ht()


def thin():
    pd()
    width(1)
    forward(15)
    ht()


# set the origin of the clock
for k in range(12):
    pu()
    left(k * 30)
    forward(200)
    thick()
    pu()
    home()

for k in range(68):
    pu()
    left(k * 6)
    forward(200)
    thin()
    pu()
    home()

mainloop()
