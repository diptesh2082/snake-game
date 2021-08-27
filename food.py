from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        X = random.randint(-380, 380)
        Y = random.randint(-380, 380)
        self.goto(X, Y)


