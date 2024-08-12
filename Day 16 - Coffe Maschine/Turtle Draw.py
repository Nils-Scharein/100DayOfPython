#Import
from turtle import Turtle, Screen
from prettytable import PrettyTable
#Setup
timmy = Turtle()
timmy.shape("turtle")
myscreen = Screen()

print(timmy)
print(myscreen)

timmy.fd(100)
timmy.rt(40)
timmy.fd(100)
myscreen.exitonclick()

x = PrettyTable()
x.field_names = ["City", "Area", "Population", "Annual"]
x.add_row(["Berlin", "Germany", 2000, 6000])
print(x)