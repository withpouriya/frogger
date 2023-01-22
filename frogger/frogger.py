import sys
import os
from random import choice, randint
import pygame
from settings import *
from player import Player
from car import Car
from all_sprites import AllSprites
from sprite import SimpleSprite, LongSprite


# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# groups
all_sprites = AllSprites()

# sprites
player = Player((500, 400), all_sprites)

# timer
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 50)
pos_list = []

# sprite setup
for file_name, pos_list in SIMPLE_OBJECTS.items():
	file_path = os.path.join('graphics', 'objects', 'simple', f'{file_name}.png')
	surf = pygame.image.load(file_path).convert_alpha()
	for pos in pos_list:
		SimpleSprite(surf, pos, all_sprites)

for file_name, pos_list in LONG_OBJECTS.items():
	file_path = os.path.join('graphics', 'objects', 'long', f'{file_name}.png')
	surf = pygame.image.load(file_path).convert_alpha()
	for pos in pos_list:
		LongSprite(surf, pos, all_sprites)

# game loop
while True:

	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == car_timer:
			random_pos = choice(CAR_START_POSITIONS)
			if random_pos not in pos_list:
				pos_list.append(random_pos)
				pos = (random_pos[0], random_pos[1] + randint(-8, 8))
				Car(pos, all_sprites)
			if len(pos_list) > 5:
				del pos_list[0]

	# delta time
	dt = clock.tick() / 1000

	# update
	all_sprites.update(dt)

	# draw
	all_sprites.customize_draw(display_surface, ((player.rect.centerx - WINDOW_WIDTH / 2, player.rect.centery - WINDOW_HEIGHT / 2)))

	# update the display surface
	pygame.display.update()
