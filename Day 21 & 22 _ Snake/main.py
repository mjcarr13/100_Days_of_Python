from turtle import Screen, Turtle
from snake import Snake
from food import Food
from border import Border
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(1200, 1200)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)
border = Border()



snake = Snake()
food = Food()
scoreboard = Scoreboard()

scoreboard.scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


game_is_on = True

speed = 0.16

while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move_snake()
    #detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend_snake()
        scoreboard.score += 1
        speed -= 0.005
        print(f"New speed: {speed}")
        food.refresh()
        scoreboard.clear()
        scoreboard.scoreboard()

    #detect collision with wall
    if (snake.head.xcor() > 290
            or snake.head.xcor() < -290
            or snake.head.ycor() > 250
            or snake.head.ycor() < -330):
        scoreboard.reset()


    #detect collission with tail
    for tail in snake.segments[1:]:
        if snake.head.distance(tail) < 15:
            scoreboard.reset()















#let's think... we want a loop or a function which will create these with these proproties
#they need to be added to a list and the all important thing is that when a new cube is
#created, we cheack the co-ordinate value of the snake cube last created and offset it by 20 pixels


#now the issue here is that sometimes we'll want the y to change as well.
#but we can work on those rules later on














screen.exitonclick()
