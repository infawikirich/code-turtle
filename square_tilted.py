import turtle

# instantiate the library
t = turtle.Pen()

win = turtle.Screen()
win.bgcolor("lightgreen")
win.setup(600, 400)

t.speed("fastest")
t.width(2)



for k in range(100):
  t.circle(100)
  t.lt(92)
  
  
  
t.ht()
turtle.mainloop()
