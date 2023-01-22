import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.image = pygame.Surface((50, 50))
		self.image.fill('red')
		self.rect = self.image.get_rect(center=pos)

		# float based movement
		self.pos = pygame.math.Vector2(self.rect.center)
		self.direction = pygame.math.Vector2((0, 1))
		self.speed = 200

	def move(self, dt):
		self.pos += self.direction * self.speed * dt
		self.rect.center = (round(self.pos.x), round(self.pos.y))

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			print('right')
		if keys[pygame.K_LEFT]:
			print('left')
		if keys[pygame.K_UP]:
			print('up')
		if keys[pygame.K_DOWN]:
			print('down')


	def update(self, dt):
		self.input()
		self.move(dt)
