import turtle

screen = turtle.Screen()
screen.bgcolor('lightgreen')

polygon = turtle.Turtle()

polygon.ht()

polygon.color('purple')
polygon.fillcolor('purple')
 
num_sides = 6
side_length = 70
angle = 360.0 / num_sides

polygon.begin_fill()
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
polygon.end_fill()

turtle.done()
