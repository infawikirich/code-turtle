"""
 script file: randomWalk.py

 purpose: This program draws a randomWalk using the turtle module

 Author: Mr. Asiamah

 Date: 25/05/21
"""

from turtle import *

import random

speed(0)
dot(5)


for i in range(5000):
    n = random.randint(1, 4)

    if n == 1:
        fd(5)
    if n == 2:
        bk(5)
    if n == 1:
        rt(90)
        fd(5)
    if n == 2:
        lt(90)
        fd(5)

dot(5)


ht()
mainloop()



