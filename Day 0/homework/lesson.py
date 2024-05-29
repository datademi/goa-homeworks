from turtle import *
speed(10)
#we want to paint house
width(5)
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
color("gray")
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

begin_fill()
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



# draw field
color("green")
begin_fill()
penup()
goto(-200 , -200)
right(90)
forward(200)
right(90)
forward(600)
right(90)
forward(200)
right(90)
forward(600)
pendown()
end_fill()
# end.
exitonclick()




