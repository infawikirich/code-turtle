"""
 script file: nautilus.py

 purpose: This program draws a nautilus using the turtle module

 Author: Mr. Asiamah

 Date: 25/05/21
"""


from turtle import *
bgcolor('lightgreen')


def square(L):
    for k in range(4):
        fd(L)
        lt(90)

width(2)
speed(0)
begin_fill()
pencolor('black')

color('navy')

end_fill()

L = 200
for k in range(100):
    square(L)
    lt(10)
    L = L * 0.98


ht()
mainloop()