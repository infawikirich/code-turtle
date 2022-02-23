"""
 script file: randomWalk.py

 purpose: This program draws a randomWalk using the turtle module

 Author: Mr. Asiamah

 Date: 25/05/21

"""

from turtle import *

import random

speed(0)



for i in range(5000):
    pencolor((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
    angle = random.randrange(360)
    fd(10)
    rt(angle)


ht()
mainloop()


