import turtle



screen = turtle.Screen()
turtle.speed(0)
turtle.hideturtle()
turtle.pencolor('yellow')
screen.bgcolor("lightblue")
turtle.pensize(2)

# turtle object
y = turtle.Turtle()

# define function
# for drawing rays of Sun
def drawFourRays(t, length, radius):
	
	for i in range(4):
		t.penup()
		t.forward(radius)
		t.pendown()
		t.forward(length)
		t.penup()
		t.backward(length + radius)
		t.left(90)


# Draw circle
# to make sun
y.penup()
y.goto(85, 110)
y.fillcolor("yellow")
y.pendown()
y.begin_fill()
y.circle(45)
y.end_fill()

# Use the defined
# function to draw rays
y.penup()
y.goto(85, 169)
y.pendown()
drawFourRays(y, 85, 54)
y.right(45)
drawFourRays(y, 85, 54)
y.left(45)

y.ht()
# To keep the
# output window active
turtle.done()
