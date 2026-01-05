from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(575, 0)
        self.penup()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(1.5,5)

    def move_up(self):
        if self.ycor() <= 430:
            self.forward(20)

    def move_down(self):
        if self.ycor() >= -430:
            self.backward(20)


