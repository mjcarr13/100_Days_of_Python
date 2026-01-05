from turtle import Turtle

class TurtleClass(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(0, -270)
        self.shapesize(1.2, 1.2)
        self.level = 0

    def move_up(self):
            new_y = self.ycor() + 10
            self.goto(self.xcor(), new_y)


    def move_down(self):
        if self.ycor() >= -270:
            new_y = self.ycor() - 10
            self.goto(self.xcor(), new_y)

    def reset_turtle(self):
        self.hideturtle()
        self.goto(0, -270)
        self.showturtle()

