import pygame

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = pygame.math.Vector2()

	def customize_draw(self, surf):

		for sprite in self.sprites():
			offset_pos = sprite.rect.topleft + self.offset
			surf.blit(sprite.image, offset_pos)
