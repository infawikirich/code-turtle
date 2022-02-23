import turtle
from turtle import *

# instantiate the screen
win = turtle.Screen()
win.bgcolor('lightgreen')
win.bgpic('park.png')


color('navy')
begin_fill()

for k in range(4):
    fd(100)
    rt(90)

end_fill()


done()
mainloop()