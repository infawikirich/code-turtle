"""
script file: captain_america_shild.py

Purpose: This program uses turtle module to create captain america
            logo

Author: Mr. Asiamah

Date : 04/03/21

"""

import turtle


# instantiate the turtle module
t = turtle.getturtle()

# instatiate the screen
win = turtle.Screen()
win.setup(800, 600)
win.title('Captain America Shield')
win.bgcolor('lightgreen')



turtle.register_shape('happy.gif')

turtle.bgpic('football_park.png')

t.shape('happy.gif')

turtle.done()