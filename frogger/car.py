import os
from random import choice
import pygame

class Car(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.name = 'car'

		for _, _, files in os.walk(os.path.join('graphics', 'cars')):
			car_name = choice(files)

		self.image = pygame.image.load(os.path.join('graphics', 'cars', car_name)).convert_alpha()
		self.rect = self.image.get_rect(center=pos)

		# float based movement
		self.pos = pygame.math.Vector2(self.rect.center)

		if pos[0] < 200:
			self.direction = pygame.math.Vector2((1, 0))
		else:
			self.direction = pygame.math.Vector2((-1, 0))
			self.image = pygame.transform.flip(self.image, True, False)

		self.speed = 300

		# collision
		self.hitbox = self.rect.inflate(0, -self.rect.height/2)

	def update(self, dt):
		self.pos += self.direction * self.speed * dt
		self.hitbox.center = (round(self.pos.x), round(self.pos.y))
		self.rect.centerx = self.hitbox.centerx

		if not -200 < self.rect.x < 3400:
			self.kill()
