import os
import pygame

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = pygame.math.Vector2()
		self.bg = pygame.image.load(os.path.join('graphics', 'main', 'map.png')).convert()
		self.fg = pygame.image.load(os.path.join('graphics', 'main', 'overlay.png')).convert_alpha()

	def customize_draw(self, surf, offset):

		self.offset.x = offset[0]
		self.offset.y = offset[1]

		surf.blit(self.bg, (-self.offset.x, -self.offset.y))

		for sprite in self.sprites():
			offset_pos = sprite.rect.topleft - self.offset
			surf.blit(sprite.image, offset_pos)

		surf.blit(self.fg, (-self.offset.x, -self.offset.y))
