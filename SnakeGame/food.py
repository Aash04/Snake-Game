from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))  # X & Y co-ordinate range (screen 600 x600)

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))