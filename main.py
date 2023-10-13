# Function excersizes drawing with turtle.

import turtle
turtle.color("red")

size = 100

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def move(len):
  back(-1 * len)

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
    
def square(size):
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)
    
def polygon(sides, len):
  for i in range(sides):
    if sides < 3:
      print("Error: Less than 3 sides!")
    else:
      turtle.forward(len)
      turtle.left(360 // sides)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)
    

#for n in range(3,10):
  #move(50)
  #polygon(n, 100 / n)
  #back(50)
  #turtle.right(360 / 7)
  



