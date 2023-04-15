from turtle import Turtle

FONT = ("Roboto", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.update_scoreboard()

    # initial code had the self.write too many times. Therefore, we need a function to do this job
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def new_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("You Gots Deaded!! Game Over!!!", align="center", font=FONT)
