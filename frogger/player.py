import os
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups, collision_sprites):
		super().__init__(groups)

		# image
		self.import_assets()
		self.frame_index = 0
		self.status = 'right'
		self.image = self.animations[self.status][self.frame_index]
		self.rect = self.image.get_rect(center=pos)

		# float based movement
		self.pos = pygame.math.Vector2(self.rect.center)
		self.direction = pygame.math.Vector2((0, 0))
		self.speed = 200

		# collisions
		self.collision_sprites = collision_sprites

	def collision(self, direction):
		if direction == 'horizontal':
			for sprite in self.collision_sprites.sprites():
				if sprite.rect.colliderect(self.rect):
					if hasattr(sprite, 'name') and sprite.name == 'car':
						print('car collision')
					if self.direction.x > 0:
						self.rect.right = sprite.rect.left
						self.pos.x = self.rect.centerx
					elif self.direction.x < 0:
						self.rect.left = sprite.rect.right
						self.pos.x = self.rect.centerx
		else:
			for sprite in self.collision_sprites.sprites():
				if sprite.rect.colliderect(self.rect):
					if hasattr(sprite, 'name') and sprite.name == 'car':
						print('car collision')
					if self.direction.y > 0:
						self.rect.bottom = sprite.rect.top
						self.pos.y = self.rect.centery
					elif self.direction.y < 0:
						self.rect.top = sprite.rect.bottom
						self.pos.y = self.rect.centery

	def import_assets(self):
		path = os.path.join('graphics', 'player')
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

		# horizontal movement + collision
		self.pos.x += self.direction.x * self.speed * dt
		self.rect.centerx = round(self.pos.x)
		self.collision('horizontal')

		# vertical movement + collision
		self.pos.y += self.direction.y * self.speed * dt
		self.rect.centery = round(self.pos.y)
		self.collision('vertical')

	def input(self):
		keys = pygame.key.get_pressed()

		# horizontal input
		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
			self.status = 'right'
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.status = 'left'
		else:
			self.direction.x = 0

		# vertical input
		if keys[pygame.K_UP]:
			self.direction.y = -1
			self.status = 'up'
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
			self.status = 'down'
		else:
			self.direction.y = 0

	def animate(self, dt):
		current_animations = self.animations[self.status]

		if self.direction.magnitude():
			self.frame_index += (8 * dt)
			self.image = current_animations[int(self.frame_index)%len(current_animations)]
		else:
			self.frame_index = 0

	def update(self, dt):
		self.input()
		self.move(dt)
		self.animate(dt)
