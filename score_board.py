from turtle import Turtle

class Score(Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"score: {self.score}",align="center", font = ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()