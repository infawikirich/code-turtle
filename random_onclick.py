#import module
import turtle, random

t = turtle.getturtle()

win = turtle.Screen()
win.bgcolor('black')

t.speed(0)

# Pen color list
colors = ['gray', 'white', 'orange', 'blue', 'yellow', 'purple']


# Define the drawing function, start drawing at the mouse click
def draw(x, y):
    t.pencolor(random.choice(colors))       # set the color of the brush
    size = random.randint(10, 40)       # draw the number of sides of the graph, use random numbers set
    t.up()
    t.goto(x, y)
    t.pd()

    for x in range(size):
        t.fd(x*2)
        t.lt(91)



turtle.onscreenclick(draw)
turtle.mainloop()

