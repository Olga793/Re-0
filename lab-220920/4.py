import pygame
from pygame.draw import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_BORDER = (255, 255, 128)
SUN_COLOR = (255, 255, 192)
SKY = (0, 255, 255)
WATER = (22, 80, 68)
GRAY = (32, 32, 32)

def draw_sun(x, y, r):
	line(screen, SUN_COLOR, (x-r, y), (x+r, y), r//10)
	line(screen, SUN_COLOR, (x, y-r), (x, y+r), r//10)
	circle(screen, SUN_BORDER, (x, y), r//10, 0)
	circle(screen, SUN_BORDER, (x, y), r, r//10)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 900))

#sky
rect(screen, SKY, (0, 0, 700, 450))
rect(screen, WHITE, (0, 450, 700, 450))
line(screen, BLACK, (0, 450), (700, 450), 1)

#sun
draw_sun(500, 200, 190)


#head
ellipse(screen, WHITE, [110, 340, 160, 80], 0)
ellipse(screen, BLACK, [110, 340, 160, 80], 1)
# mouth
ellipse(screen, BLACK, [190, 387, 75, 10], 1)
rect(screen, WHITE, [190, 387, 75, 5], 0)
#eyes
circle(screen, BLACK, (260, 370), 5, 0)
circle(screen, BLACK, (210, 370), 5, 0)
#ear
circle(screen, WHITE, (135, 355), 15, 0)
circle(screen, BLACK, (135, 355), 15, 1)
rect(screen, WHITE, [127, 353, 25, 20], 0)

#body
ellipse(screen, WHITE, [20, 400, 200, 400], 0)
ellipse(screen, BLACK, [20, 400, 200, 400], 1)

#hole
ellipse(screen, GRAY, [355, 635, 260, 70], 0)
ellipse(screen, WATER, [385, 650, 200, 50], 0)

#fishing rod
line(screen, BLACK, (210, 605), (490, 325), 5)
line(screen, BLACK, (485, 330), (485, 700), 1)
#hand
ellipse(screen, WHITE, [180, 500, 120, 50], 0)
ellipse(screen, BLACK, [180, 500, 120, 50], 1)

#leg
ellipse(screen, WHITE, [120, 700, 150, 100], 0)
ellipse(screen, BLACK, [120, 700, 150, 100], 1)
ellipse(screen, WHITE, [235, 750, 75, 50], 0)
ellipse(screen, BLACK, [235, 750, 75, 50], 1)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.time.get_ticks() > 5000):
            finished = True

pygame.quit()
