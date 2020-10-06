import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
arial = pygame.font.SysFont("Arial Black", 64)

def new_ball():
	#рисует новый шарик
	x = randint(100, 1100)
	y = randint(100, 900)
	r = randint(10, 100)
	color = COLORS[randint(0, 5)]
	circle(screen, color, (x, y), r)
	return((x,y,r))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0

while not finished:
	clock.tick(FPS)
	clicked = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos
			if ((not clicked) and ((x-xpos)**2 + (y-ypos)**2 <= r*r)):
				print('Click true!')
				score += 100//r
				clicked = True
			else:
				print('Click.')
			#circle(screen, RED, event.pos, 10)

	screen.fill(BLACK)

	xpos,ypos,r = new_ball()

	text = arial.render(str(score), True, WHITE)
	screen.blit(text, (0, 0))
	pygame.display.update()


pygame.quit()
