from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
	screen.update()
	time.sleep(0.10)
	snake.move()

	#detect food collision
	if snake.head.distance(food) < 15:
		food.refresh()
		score.increase_score()
		snake.extend()

	#detect wall collision
	if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
		game_on = False
		score.game_over()

	#detect collision with tail
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			game_on = False
			score.game_over()

screen.exitonclick()
