"""
    script file: sixteen_petal_flower.py

    Purpose: This program uses turtle draw to sixteen petal flower

    Author: Mr. Asiamah

    Date: 08/06/21
"""

import turtle
turtle.title('Sixteen Petals')
turtle.setworldcoordinates(-2000, -2000, 2000, 2000)


def draw_football(x, y, tilt, radius):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(tilt - 45)
    turtle.circle(radius, 90)
    turtle.left(90)
    turtle.circle(radius, 90)

for tilt in range(0, 360, 30):
    draw_football(0,0, tilt, 1000)


turtle.ht()
turtle.mainloop()