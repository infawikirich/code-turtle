"""
script file: sin_graph.py

Purpose: This program uses turtle to draw turtle graph
Author: Mr. Asiamah

Date : 03/04/21

"""

import turtle, math


# instantiate the turtle module
t = turtle.getturtle()

# instatiate the screen
win = turtle.Screen()
win.setup(800, 600)
win.title('Sin Graph')
win.bgcolor('black')

t = turtle.getturtle()
win = turtle.Screen()
win.setup(960, 720)

turtle.bgcolor('lightgreen')

t.pencolor('red')
t.pensize(2)
t.speed(0)

initial_value = 0
final_value = 100 * math.pi
steps = (final_value - initial_value) / 500
x_values = []

# Calculate the x values
for k in range(1000):
    initial_value = initial_value + steps
    x_values.append(initial_value)

# Calculate the y values
y_values = []
for k in range(1000):
    y_values.append(100 * math.sin(x_values[k] / (10 * math.pi)))

for i in range(1000):
    t.goto(x_values[i], y_values[i])

turtle.mainloop()
