from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.x_serve = 10

    def serve_ball(self):
        new_x = self.xcor() + self.x_serve
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_serve *= -1

    def serve_reset(self):
        self.x_serve *=-1





    # def serve_ball(self):
    #     while 380 > self.xcor() > -380:
    #         if self.ycor() < 280 and self.ycor() > -280:
    #             new_x = self.xcor() + 10
    #             new_y = self.ycor() + 10
    #             self.goto(new_x, new_y)
    #         else:
    #             new_x = self.xcor() + 10
    #             new_y = self.ycor() - 10
    #             self.goto(new_x, new_y)