from turtle import Screen
import time
from mainsnake import Snake
from food import Food
from scoorbord import Scoreboard


screen=Screen()
screen.bgcolor("black")
screen.setup(height=800, width=800)

screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scoreincrease()

    if snake.head.xcor()>= 400 or snake.head.xcor()<=-400 or snake.head.ycor()>= 400 or snake.head.ycor() <= -400:
        score.reset_scoreboard()
        snake.reset()
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            score.reset_scoreboard()
            snake.reset()


screen.exitonclick()



