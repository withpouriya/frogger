import os
from random import choice
import pygame

class Car(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		for _, _, files in os.walk(os.path.join('graphics', 'cars')):
			car_name = choice(files)

		self.image = pygame.image.load(os.path.join('graphics', 'cars', car_name)).convert_alpha()
		self.rect = self.image.get_rect(center=pos)

