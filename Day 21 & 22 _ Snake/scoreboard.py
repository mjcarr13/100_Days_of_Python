from turtle import Turtle

ALIGNMENT = "center"
FONT = "256 Bytes"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(-160, 260)
        self.high_score = 0
        self.score = 0

    def scoreboard(self):
        self.write(arg=f"Score: {self.score}"
                       f"High Score: {self.high_score}",
                 move = False,
                 align= ALIGNMENT,
                 font = (FONT, 40, 'normal')
                   )


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

