"""
 script file: star.py

 purpose: This program draws a radiating star using the turtle module

 Author: Mr. Asiamah

 Date: 25/05/21
"""

from turtle import *

def star(n, r):         # n is the number of the radiating rays, r is the length of the star
    """This function draws a star of rays of length r"""

    for k in range(0, n):
        pendown()
        fd(r)
        up()
        bk(r)
        lt(360/n)



width(3)
star(20, 200)

ht()
mainloop()