from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake
from border import Border

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 600 , height = 600)
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Border()
border.move()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15 :
        food.refrash()
        snake.extend()
        scoreboard.increase_score()
    #detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280 :
        scoreboard.game_over()
        game_is_on = False
    #detect collision with tail
    for segment in snake.segments[1:] :
        if snake.head.distance(segment) < 10 :
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()