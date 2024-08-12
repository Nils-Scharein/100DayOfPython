from turtle import Turtle, Screen

#start Code
turtle = Turtle()
turtle.shape("arrow")
screen = Screen()
turtle.pensize(5)
a = 10

def forward_click():
    turtle.fd(a)

def backwards_click():
    turtle.bk(a)

def right_click():
    turtle.rt(a)

def left_click():
    turtle.lt(a)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.onkeypress(forward_click, "Up")
screen.onkeypress(backwards_click, "Down")
screen.onkeypress(right_click, "Right")
screen.onkeypress(left_click, "Left")
screen.onkeypress(clear, "c")
screen.listen()
screen.exitonclick()

