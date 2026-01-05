from turtle import Screen, Turtle
from gridlines import draw_gridlines
from paddle import Paddle
screen = Screen()
screen.setup(width=1200, height=900)
screen.setworldcoordinates(-600, -450, 600, 450)
screen.bgcolor("black")
screen.title("PONG")

draw_gridlines()
paddle1 = Paddle()
paddle2 = Paddle()
paddle2.goto(0,-430)


screen.listen()

screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

















screen.exitonclick()