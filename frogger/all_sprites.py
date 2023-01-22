import pygame

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

	def customize_draw(self, surf):
		for sprite in self.sprites():
			surf.blit(sprite.image, sprite.rect)
