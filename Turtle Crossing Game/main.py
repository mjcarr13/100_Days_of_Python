from turtle import Screen
from turtle_class import TurtleClass
from cars import Car
from scoreboard import Scoreboard

import time

screen = Screen()
screen.tracer(0)

screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle Game")
screen.listen()


turtle = TurtleClass()
cars = Car()
level = Scoreboard()

screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")


game_on = True
speed = 0.2


while game_on:
    screen.update()
    time.sleep(speed)
    cars.cars_move()
    level.scoreboard()
    if turtle.ycor() >= 270:
        level.level += 1
        level.clear()
        level.scoreboard()
        speed *= 0.9
        turtle.reset_turtle()
        cars.refresh()

    for car in cars.all_cars[0:]:
        if turtle.distance(car) < 30:
            level.game_over()
            game_on = False


screen.exitonclick()
