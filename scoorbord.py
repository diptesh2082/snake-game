from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score} " f" High Score = {self.highscore}", align="center",
                   font=("Arial", 15, "normal"))

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 25, "normal"))

    def scoreincrease(self):
        self.score += 1
        self.clear()
        self.update()
