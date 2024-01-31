from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.hideturtle()
        self.teleport(0, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_score()
