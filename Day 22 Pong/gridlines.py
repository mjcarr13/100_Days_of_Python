from turtle import Turtle

def draw_gridlines():
    gridlines = Turtle()
    gridlines.penup()
    gridlines.speed("fastest")
    gridlines.hideturtle()
    gridlines.color("white")
    gridlines.pensize(3)
    gridlines.goto(0,430)
    gridlines.setheading(270)
    for _ in range(22):
        gridlines.pendown()
        gridlines.forward(20)
        gridlines.penup()
        gridlines.forward(20)




