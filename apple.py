from turtle import Turtle
import random
import time

class Apple(Turtle):
    def __init__ (self):
        super().__init__ ("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5,0.5)
        self.appear_in_rand()

    def appear_in_rand(self):
        self.hideturtle()
        # time.sleep(2)
        random_x = random.randint(-380,380)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)
        self.showturtle()
        
