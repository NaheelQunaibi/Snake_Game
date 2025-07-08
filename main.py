from turtle import Turtle, Screen
from apple import Apple
from snake import Snake
from score_board import Score
import time

def game_over():
    result = Turtle()
    result.penup()
    result.goto(0,0)
    result.hideturtle()
    result.write(f"Game Over\nfinal score {score.score}",align="center",font=("Arial", 40, "normal"))

window = Screen()
window.bgcolor("lightgreen")
window.setup(800,600)
window.title("snake game")
window.tracer(0)

dodo = Snake()
window.update()
time.sleep(0.1)

apple = Apple()
score = Score()

game_on = True
while game_on:
    dodo.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(dodo.down,"Down")
    window.onkey(dodo.up,"Up")
    window.onkey(dodo.right,"Right")
    window.onkey(dodo.left,"Left")

    if dodo.head.distance(apple) <= 15:
        apple.appear_in_rand()
        dodo.extend()
        score.increase_score()

    if dodo.head.xcor() > 390 or dodo.head.xcor() < -390 or dodo.head.ycor() > 290 or dodo.head.ycor() < -290:
        game_over()
        game_on = False

    for segment in dodo.turtles[:-1]:
        if dodo.head.distance(segment) <= 10:
            game_over()
            game_on = False

window.exitonclick()