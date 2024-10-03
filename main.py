import turtle as t
from snake import Snake
from food import Food
from scoreboard import  Scoreboard
#import random
import time


screen=t.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game - StephaGonz")
screen.tracer(0)


snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_animation()
    #food collision
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.score_increment()
    #wall collision

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        is_game_on=False
        score.game_over()
    #tail collision

    for segment in snake.segments_list[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            score.game_over()



screen.exitonclick()