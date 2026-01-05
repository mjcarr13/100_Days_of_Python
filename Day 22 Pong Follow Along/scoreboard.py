from turtle import Turtle

ALIGNMENT = "center"
FONT = "256 Bytes"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(-310, 230)
        self.score = 0

    def scoreboard(self):
        self.write(arg=f"{self.score}",
                 move = False,
                 align= ALIGNMENT,
                 font = (FONT, 50, 'normal')
                   )
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER",
                   move=False,
                   align=ALIGNMENT,
                   font=(FONT, 50, 'normal')
                   )
