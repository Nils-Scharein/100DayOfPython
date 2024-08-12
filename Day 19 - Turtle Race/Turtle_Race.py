import turtle
from turtle import Turtle, Screen
import random

#allgemeine variablen
turtles = []
x = -240
y = -150
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtles = []

#Setup Screen
screen = Screen()
screen.setup(width = 500, height = 400)

#Methoden
def player_input():
    while True:
        input = turtle.textinput("Which Turtle will win?", f"{colors}?").lower()
        if input in colors:
            return input

def random_move(turtle):
    turtle.fd(random.randint(1, 10))

input = player_input()


def spawn_all():
    for index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[index])
        new_turtle.goto(x=-230, y=y_pos[index])
        turtles.append(new_turtle)

spawn_all()

def main():
    if input:
        is_race_on = True
    while is_race_on:
        for turtle in turtles:
            random_move(turtle)
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == input:
                    print(f"Your Turtle {input} won.")
                else:
                    print(f"Your Turtle {input} lost, the winner was {winning_color}")

main()
screen.exitonclick()