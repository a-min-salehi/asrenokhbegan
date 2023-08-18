import turtle
import math
import random
import requests

screen = turtle.Screen()
screen.bgcolor('lightblue')
turtle.speed(0)
turtle.pensize(2)
y = turtle.Turtle()


def sunny():
    turtle.ht()
    turtle.pencolor('yellow')

    def drawFourRays(t, length, radius):
        for i in range(4):
            t.penup()
            t.forward(radius)
            t.pendown()
            t.forward(length)
            t.penup()
            t.backward(length + radius)
            t.left(90)

    y.ht()
    y.penup()
    y.goto(85, 110)
    y.fillcolor("yellow")
    y.pendown()
    y.begin_fill()
    y.circle(45)
    y.end_fill()
    y.penup()
    y.goto(85, 169)
    y.pendown()
    drawFourRays(y, 85, 54)
    y.right(45)
    drawFourRays(y, 85, 54)
    y.left(45)
    y.ht()
    turtle.done()


def rainy():
    turtle.hideturtle()
    y.pencolor('blue')
    y.ht()
    y.penup()
    y.goto(-200, 0)
    y.seth(90)
    y.pensize(1)
    y.fillcolor('yellow')
    y.begin_fill()
    y.pd()
    y.circle(radius=-330, extent=66)
    y.goto(0, 300)
    y.seth(233)
    y.circle(radius=500, extent=38)
    y.goto(-100, 0)
    y.seth(90)
    y.circle(50, 180)
    y.end_fill()
    y.penup()
    y.goto(-100, 0)
    y.seth(90)
    y.pensize(1)
    y.fillcolor('red')
    y.begin_fill()
    y.pd()
    y.circle(radius=-500, extent=37)
    y.goto(0, 300)
    y.seth(270)
    y.pensize(3)
    y.forward(300)
    y.seth(90)
    y.pensize(1)
    y.circle(50, 180)
    y.end_fill()
    y.penup()
    y.goto(100, 0)
    y.seth(90)
    y.pensize(1)
    y.fillcolor('blue')
    y.begin_fill()
    y.pd()
    y.circle(radius=500, extent=37)
    y.goto(0, 300)
    y.seth(270)
    y.pensize(3)
    y.forward(300)
    y.seth(90)
    y.pensize(1)
    y.circle(-50, 180)
    y.end_fill()
    y.penup()
    y.goto(200, 0)
    y.seth(90)
    y.pensize(1)
    y.fillcolor('pink')
    y.begin_fill()
    y.pd()
    y.circle(radius=330, extent=66)
    y.goto(0, 300)
    y.seth(-53)
    y.circle(radius=-500, extent=37)
    y.goto(100, 0)
    y.seth(90)
    y.circle(-50, 180)
    y.end_fill()
    y.penup()
    y.goto(200, 0)
    y.fillcolor('lightgreen')
    y.begin_fill()
    y.seth(90)
    y.pensize(1)
    y.pd()
    y.pencolor('blue')
    y.circle(radius=330, extent=66)
    y.goto(0, 300)
    y.seth(0)
    y.circle(-300, 90)
    y.seth(90)
    y.circle(50, 180)
    y.end_fill()
    y.pu()
    y.goto(0, 300)
    y.seth(90)
    y.pensize(9)
    y.pd()
    y.pencolor('black')
    y.forward(20)
    y.pu()
    y.seth(270)
    y.pensize(5)
    y.forward(310)
    y.pd()
    y.forward(290)
    y.pensize(8)
    y.forward(10)
    y.circle(20, 180)
    y.penup()
    y.hideturtle()
    turtle.done()


def cloudy():
    turtle.hideturtle()
    turtle.penup()
    turtle.pencolor('white')

    n = 500

    def ellipse(X, Y, a, b, ts, te, P):
        t = ts
        for i in range(n):
            x = a * math.cos(t)
            yy = b * math.sin(t)
            P.append((x + X, yy + Y))
            t += (te - ts) / (n - 1)

    def dist(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def draw_arc(p1, p2, ext):
        turtle.penup()
        turtle.goto(p1)
        turtle.seth(turtle.towards(p2))
        a = turtle.heading()
        b = 360 - ext
        c = (180 - b) / 2
        d = a - c
        e = d - 90
        r = dist(p1, p2) / 2 / math.sin(math.radians(b / 2))
        turtle.seth(e)
        turtle.down()
        turtle.circle(r, ext, 100)
        return turtle.xcor(), turtle.ycor()

    def cloud(P):
        step = n // 10
        a = 0
        b = a + random.randint(step // 2, step * 2)
        p1 = P[a]
        p2 = P[b]
        turtle.fillcolor('white')
        turtle.begin_fill()
        p3 = draw_arc(p1, p2, random.uniform(70, 180))
        while b < len(P) - 1:
            p1 = p3
            if b < len(P) / 2:
                ext = random.uniform(70, 180)
                b += random.randint(step // 2, step * 2)
            else:
                ext = random.uniform(30, 70)
                b += random.randint(step, step * 2)
            b = min(b, len(P) - 1)
            p2 = P[b]
            p3 = draw_arc(p1, p2, ext)
        turtle.end_fill()
        turtle.done()

    P = []
    ellipse(0, 0, 300, 200, 0, math.pi, P)
    ellipse(0, 0, 300, 50, math.pi, math.pi * 2, P)
    cloud(P)


params = {
    'access_key': '7f98192797a8978433ec110098505805',
    'query': 'London'
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()

city = params['query']

condition = api_response['current']['weather_descriptions'][0]

temperature = api_response['current']['temperature']

print(city, temperature, '°C')

if 'Sun' in condition:
    sunny()
elif 'Rain' in condition:
    rainy()
else:
    cloudy()

