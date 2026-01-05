import colorgram
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)


# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 20)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

rgb_colors = [(249, 228, 17), (236, 255, 236), (213, 13, 9), (197, 13, 35), (196, 70, 21), (229, 228, 6), (235, 148, 38), (33, 90, 188), (44, 212, 70), (33, 30, 152), (16, 22, 54), (67, 9, 49), (238, 244, 250), (243, 39, 149), (14, 206, 223), (67, 202, 229), (63, 21, 11), (224, 20, 112)]

tim = Turtle()
tim.speed("fastest")
tim.pensize(20)
tim.penup()
tim.hideturtle()


for _ in range(5):
    for _ in range(10):
        tim.dot(random.choice(rgb_colors))
        tim.forward(70)
    tim.left(90)
    tim.forward(70)
    tim.dot(random.choice(rgb_colors))
    tim.left(90)
    for _ in range(10):
        tim.forward(70)
        tim.dot(random.choice(rgb_colors))
    tim.right(90)
    tim.forward(70)
    tim.dot(random.choice(rgb_colors))
    tim.right(90)






tim.dot(random.choice(rgb_colors))

#so turtle needs to begin with a random color
#draw a circle where it stands
#it then moves 50 places over to the right and repeats
#it does this 10 times in total
# it then moves up 50 places
#draws a dot
#it then moves 50 places over to the left and repeats
#the above process occurs 5 times


screen = Screen()
screen.setup(width=1000,height=1000)
screen.exitonclick()