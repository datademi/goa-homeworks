from turtle import *
speed(10)
width(9)






color("blue")
#step 1 draw a square 
shape("turtle")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90) 
end_fill()
#end square

forward (75)

 
 # draw door 
begin_fill()
color("green")
left(90)
forward(120)
right(90)
forward(50)
right(90)
forward(120)

end_fill()
penup()
goto(200 , 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(60)
# draw windows 
begin_fill()
color("purple")
penup()
goto( 25 , 160)
left(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

begin_fill() #
penup()
goto(150 , 160)
right(180)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()
 # end drawing first house

#start drawing second house
begin_fill() # drawing square
goto(-100 , 200)
pendown()
end_fill()

shape("turtle")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90) 
end_fill()

color("orange") #drawing a roof
begin_fill()

right(60)
forward(180)
left(115)
forward(190)
right(90)
end_fill()

penup() #drawing a door
goto(-225, 0 )
pendown()
color("yellow")
begin_fill()
right(55)
forward(120)
right(90)
forward(55)
right(90)
forward(120)
right(90)
forward(55)
end_fill()

# start drawing windows
penup()# first
goto(-275, 150)
pendown()
color("magenta")
begin_fill()
left(180)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
end_fill()

penup()#second
goto(-150 , 150)
pendown()
color("magenta")
begin_fill()
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
end_fill()
# end second house

#start third house
left(90)
penup()
forward(250)
right(90)
forward(50)
left(90)
pendown()
# start drawing square

color("cyan")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#finish square

# start drawing roof
color("black")
begin_fill()
right(60)
forward(200)
left(120)
forward(200)
end_fill()
# end drawing roof
#draw door 
color("red")
penup()
left(30)
forward(200)
left(90)
forward(65)
pendown()
begin_fill()
left(90)
forward(120)
right(90)
forward(65)
right(90)
forward(120)
right(90)
forward(65)
end_fill()
# finish door 

# start drawing windows
penup() # first
color("pink")
begin_fill()
goto(-450 , 150)
pendown()
right(180)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
end_fill()

penup() #second
color("pink")
begin_fill()
goto(-550 , 150)
pendown()
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
end_fill()



penup()
goto(450,300)
pendown()
color("yellow")
begin_fill()
right (40)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
right(30)
forward(30)
end_fill()

import turtle

import math 

  

  
# Function to draw rectangle 
penup()
goto(-300 , -300)
pendown()
def drawRectangle(t, width, height, color): 

    t.fillcolor(color) 

    t.begin_fill() 

    t.forward(width) 

    t.left(90) 

    t.forward(height) 

    t.left(90) 

    t.forward(width) 

    t.left(90) 

    t.forward(height) 

    t.left(90) 

    t.end_fill() 

  

      
# Function to draw triangle     

def drawTriangle(t, length, color): 

    t.fillcolor(color) 

    t.begin_fill() 

    t.forward(length) 

    t.left(135) 

    t.forward(length / math.sqrt(2)) 

    t.left(90) 

    t.forward(length / math.sqrt(2)) 

    t.left(135) 

    t.end_fill() 

  

      
# Set the background color 

screen = turtle.Screen ( ) 

screen.bgcolor("skyblue") 

  

  
# Creating turtle object 

tip = turtle.Turtle() 

tip.color ("black") 

tip.shape ("turtle") 

tip.speed (2) 

  

  
# Tree base 
tip.penup() 

tip.goto(100, -130) 
tip.pendown() 

drawRectangle(tip, 20, 40, "brown") 

  

  
# Tree top 
tip.penup() 

tip.goto(65, -90) 
tip.pendown() 

drawTriangle(tip, 90, "lightgreen") 
tip.penup() 

tip.goto(70, -45) 
tip.pendown() 

drawTriangle(tip, 80, "lightgreen") 
tip.penup() 

tip.goto(75, -5) 
tip.pendown() 

drawTriangle(tip, 70, "lightgreen")















exitonclick()