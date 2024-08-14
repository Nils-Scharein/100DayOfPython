import colorgram
import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")

screen = Screen()
screen.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb = color.rgb
    r, g, b = rgb
    rgb_colors.append((r, g, b))

colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
print(rgb_colors)

def dashed_line(distance, number, size):
    turtle.penup()
    turtle.pensize(size)
    for i in range(0, number):
        turtle.dot(random.choice(colors))
        turtle.fd(distance)

def painting(distance, rows, collums, size):
    for i in range(0, rows):
        turtle.pendown()
        position = turtle.pos()
        x, y = position
        dashed_line(distance, collums, size)
        turtle.penup()
        turtle.setpos(x, y + distance)

turtle.penup()
turtle.setpos(-150, -100)
painting(50, 5, 5, 20)
screen.exitonclick()