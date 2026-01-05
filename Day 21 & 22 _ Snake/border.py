from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("White")
        self.penup()
        self.draw_border()

    def draw_border(self):
        self.goto(-290, 250)
        self.pendown()
        self.goto(290, 250)
        self.goto(290, -330)
        self.goto(-290, -330)
        self.goto(-290, 250)
