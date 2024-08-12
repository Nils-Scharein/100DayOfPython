from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

screen = Screen()
screen.colormode(255)

len = 200
distance = 50
size = 2
colours = ["red", "blue", "green", "purple", "Yellow", "black"]
directions = [0, 90, 180, 270]

def square(len):
    for i in range(4):
        turtle.fd(len)
        turtle.lt(90)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def dashed_line(distance, number):
    for i in range(0, number):
        turtle.fd(distance)
        turtle.penup()
        turtle.fd(distance)
        turtle.pendown()


#dashed_line(5, 20)
def draw_shapes():
    shapes = 6
    sides = 3
    distance = 150
    for shape in range(0, shapes):
        degree = 360/sides
        turtle.color(random.choice(colours))
        for side in range(0, sides):
            turtle.fd(distance)
            turtle.rt(degree)
        sides += 1

def random_walk(loop, len, thicc):
    turtle.pensize(thicc)
    turtle.speed("fastest")
    for i in range(0, loop):
        turtle.color(random_color())
        turtle.fd(len)
        turtle.rt(random.choice(directions))

def circle(circles, big):
    turtle.speed("fastest")
    for i in range(0, circles):
        turtle.pencolor(random_color())
        turtle.circle(big)
        turtle.rt(360 / circles)

circle(55, 200)

#random_walk(200, 50, 20)





screen.exitonclick()