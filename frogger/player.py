import os
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)

		# image
		self.import_assets()
		self.frame_index = 0
		self.image = self.animation[self.frame_index]
		self.rect = self.image.get_rect(center=pos)

		# float based movement
		self.pos = pygame.math.Vector2(self.rect.center)
		self.direction = pygame.math.Vector2((0, 0))
		self.speed = 200

	def import_assets(self):
		path = os.path.join('data', 'graphics', 'player', 'right')
		self.animation = [pygame.image.load(os.path.join(path, f'{frame}.png')).convert_alpha() for frame in range(4)]
		print(self.animation)

	def move(self, dt):
		if self.direction.magnitude():
			self.direction = self.direction.normalize()

		self.pos += self.direction * self.speed * dt
		self.rect.center = (round(self.pos.x), round(self.pos.y))

	def input(self):
		keys = pygame.key.get_pressed()

		# horizontal input
		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		# vertical input
		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

	def animate(self, dt):
		self.frame_index += (8 * dt)
		self.image = self.animation[int(self.frame_index)%len(self.animation)]

	def update(self, dt):
		self.input()
		self.move(dt)
		self.animate(dt)
