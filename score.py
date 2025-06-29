from turtle import Turtle

FONT = ('Courier', 18, 'normal')

class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.ht()
		self.penup()
		self.color("white")
		self.speed("fastest")
		self.goto(0, 270)
		self.write_score()

	def write_score(self):
		self.clear()
		current_score = f"Score: {self.score}"
		self.write(current_score, align="center", font=FONT)
	
	def increase_score(self):
		self.score += 1
		self.write_score()

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align="center", font=FONT)