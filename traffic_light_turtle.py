# import turtle
import turtle

t = turtle.getturtle()

# create an object of the Screen
win = turtle.Screen()
win.title('Contructing Traffic Light')
win.bgcolor('lightgreen')

def draw_housing():
    """Draw a nice housing to hold the traffic light"""
    t.pensize(3)
    t.color('black', 'darkgray')
    t.begin_fill()
    t.fd(80)
    t.lt(90)
    t.fd(200)
    t.circle(40, 180)
    t.fd(200)
    t.lt(90)
    t.end_fill()

draw_housing()

t.up()
# Position turtle onto the place where the green light should be
t.fd(40)
t.lt(90)
t.fd(50)
# Turn turtle to into a big green circle
t.shape('circle')
t.shapesize(4, 4, 2 )
t.fillcolor('green')

# A traffic light is a kind of state machine with three states,
# Green, Orange, REd. We number these states 0, 1, 2 when the
# machine changes state, we change turtle position and the fillcolor

# This variable holds the current stat of the machine
state_num = 0

def advance_state_machine():
    global state_num

    if state_num == 0:          # Transition from state 0 to 1
        t.fd(70)
        t.fillcolor('orange')
        state_num = 1
    elif state_num == 1:        # Transition from state 1 to state 2
        t.fd(70)
        t.fillcolor('red')
        state_num = 2
    else:                       # Transition from 2 to state 0
        t.back(140)
        t.fillcolor('green')
        state_num = 0


# Bind the event handler to the space key
win.onkey(advance_state_machine, 'space')
win.listen()

turtle.mainloop()