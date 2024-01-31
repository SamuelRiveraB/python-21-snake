from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.teleport(0, 260)
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.teleport(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)