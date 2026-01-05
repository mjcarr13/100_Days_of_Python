from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
P1_score = Scoreboard()
P1_score.scoreboard()
P2_score = Scoreboard()
P2_score.goto(310,230)
P2_score.scoreboard()


screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True

speed = 0.1

while game_on:
        screen.update()
        time.sleep(speed)
        ball.serve_ball()
        #detect collision with ceiling
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        #detect collision with right paddle
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
                or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()
        #if paddle misses ball, serve again to other side
        elif ball.xcor() > 380:
            ball.goto(0,0)
            ball.serve_reset()
            P1_score.score += 1
            P1_score.clear()
            P1_score.scoreboard()
            speed -= 0.01
            ball.serve_ball()
        elif ball.xcor() < -380:
            ball.goto(0,0)
            ball.serve_reset()
            P2_score.score += 1
            P2_score.clear()
            P2_score.scoreboard()
            speed -= 0.01
            ball.serve_ball()
        if P1_score.score >= 5 or P2_score.score >= 5:
            game_on = False







screen.exitonclick()

