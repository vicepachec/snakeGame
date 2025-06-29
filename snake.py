from turtle import Turtle

#Constants make it easier to tweak the game
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	def __init__(self):
		self.segments = []
		self.snake_maker()
		self.head = self.segments[0]
	
	def snake_maker(self):
		for position in STARTING_POSITIONS:
			self.add_segment(position)

	def add_segment(self, position):
		new_turtle = Turtle(shape="square")
		new_turtle.color("white")
		new_turtle.penup()
		new_turtle.goto(position)
		self.segments.append(new_turtle)

	def extend(self):
		self.add_segment(self.segments[-1].position())

	def move(self):
		for index in range(len(self.segments) - 1, 0, -1):
			pos = self.segments[index - 1].position()
			self.segments[index].goto(pos)
		self.head.fd(MOVE_DISTANCE)
	
	def up(self):
		if self.head.heading() != DOWN:
			self.head.seth(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.seth(DOWN)
	
	def left(self):
		if self.head.heading() != RIGHT:
			self.head.seth(LEFT)
	
	def right(self):
		if self.head.heading() != LEFT:
			self.head.seth(RIGHT)