import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Pong"

class Game(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		arcade.set_background_color(arcade.color.BLACK)

		self.my_ball = Ball()
		self.my_paddle = Paddle()
	def on_key_press(self, key, key_modifiers):
		pass
	def on_key_release(self, key, key_modifiers):
		pass
	def on_update(self, delta_time):
		pass

	def on_draw(self):
		arcade.start_render()
		self.my_ball.on_draw()
		self.my_paddle.on_draw()
class Ball():
	def __init__(self):
		self.x = 300
		self.y = 300
		self.radius = 20
		self.color = arcade.color.WHITE
	def on_draw(self):
		arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
class Paddle():
	def __init__(self):
		self.x = 989
		self.y = 450
		self.width = 10
		self.height = 180
		self.color = arcade.color.WHITE
	def on_draw(self):
		arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

def main():
	""" Main method """
	game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	arcade.run()


if __name__ == "__main__":
	main()