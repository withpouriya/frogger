import os
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)

		# image
		self.import_assets()
		self.frame_index = 0
		self.status = 'up'
		self.image = self.animations[self.status][self.frame_index]
		self.rect = self.image.get_rect(center=pos)

		# float based movement
		self.pos = pygame.math.Vector2(self.rect.center)
		self.direction = pygame.math.Vector2((0, 0))
		self.speed = 200

	def import_assets(self):
		path = os.path.join('data', 'graphics', 'player')
		self.animations = {}

		for index, folder in enumerate(os.walk(path)):
			if index == 0:
				for name in folder[1]:
					self.animations[name] = []
			else:
				for file in folder[2]:
					file = os.path.join(folder[0], file)
					surf = pygame.image.load(file).convert_alpha()
					self.animations[os.path.basename(os.path.dirname(file))].append(surf)

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
		current_animations = self.animations[self.status]
		self.frame_index += (8 * dt)
		self.image = current_animations[int(self.frame_index)%len(current_animations)]

	def update(self, dt):
		self.input()
		self.move(dt)
		self.animate(dt)
