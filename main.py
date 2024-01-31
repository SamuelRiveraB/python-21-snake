from turtle import Screen
import time

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scoreboard = ScoreBoard()

game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
