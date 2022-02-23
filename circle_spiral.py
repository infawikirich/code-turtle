import turtle


win = turtle.Screen()
win.title("Circle Spiral")
win.bgcolor("lightgreen")


turtle.speed("fastest")
turtle.pensize(2)
turtle.pencolor("red")



for k in range(100):
  turtle.circle(100)
  turtle.right(91)
  
  
  
turtle.mainloop()
