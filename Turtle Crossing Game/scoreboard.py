from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.level = 1

    def scoreboard(self):
        self.write(arg=f"LEVEL: {self.level}",
                 move = False,
                 align= ALIGNMENT,
                 font = (FONT, 30, 'normal')
                   )
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER",
                   move=False,
                   align=ALIGNMENT,
                   font=(FONT, 50, 'normal')
                   )
