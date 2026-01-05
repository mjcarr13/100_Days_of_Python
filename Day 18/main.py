import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


tim = Turtle()
tim.shape("turtle")
tim.color("red")
#
# #create list of angle sizes for each shape
# shape_exterior_angles = [120, 90, 72, 60, 51.43, 45, 40, 36]
# #create colour list from which turtle can randomly draw


#programme movements,
#
# #slect random turtle colour
# tim.goto(0,0)
# for i, angle in enumerate(shape_exterior_angles):
#     tim.color(random.choice(colours))
#     for _ in range (i+3):
#         tim.forward(100)
#         tim.left(angle)



#random walk

# def random_walk():
#     tim.speed(0)
#     tim.pensize(8)
#     directions = [0,90,180,270]
#     for _ in range(200):
#         tim.color(random_colour())
#         tim.setheading(random.choice(directions))
#         tim.forward(30)
#
# random_walk()

# #turtle changes colour
# tim.color(random.choice(colours))
# #turtle turns right one of four angles randomly, 90, 180, 270, 360
# tim.right(random.choice(directions))
# #turtle moves forwards by 10
# tim.forward(10)
# #repeat


for _ in range(120):
    tim.speed("fastest")
    tim.pensize(1)
    tim.color(random_colour())
    tim.circle(150)
    tim.right(3)

screen = Screen()
screen.exitonclick()
