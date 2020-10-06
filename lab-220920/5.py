import pygame
from pygame.draw import *
from numpy import pi

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

def draw_hole(x, y, r):
	ellipse(screen, GRAY, [x-(5*r)//2, y-(3*r)//4, 5*r, (11*r)//8], 0)
	ellipse(screen, WATER, [x-2*r, y-r//2, 4*r, r], 0)

def draw_head(x=110, y=340):
	ellipse(screen, WHITE, [x, y, 160, 80], 0)
	ellipse(screen, BLACK, [x, y, 160, 80], 1)
	# mouth
	ellipse(screen, BLACK, [x+80, y+47, 75, 10], 1)
	rect(screen, WHITE, [x+80, y+47, 75, 5], 0)
	#eyes
	circle(screen, BLACK, (x+150, y+30), 5, 0)
	circle(screen, BLACK, (x+100, y+30), 5, 0)
	#ear
	circle(screen, WHITE, (x+25, y+15), 15, 0)
	circle(screen, BLACK, (x+25, y+15), 15, 1)
	rect(screen, WHITE, [x+17, y+13, 25, 20], 0)

def draw_ear(x, y, r):
	circle(screen, WHITE, (x, y), r, 0)
	circle(screen, BLACK, (x, y), r, 1)
	rect(screen, WHITE, [x-r//2, y, r+r//2, r], 0)

def draw_head_2(x, y, r):
	ellipse(screen, WHITE, [x, y, 6*r, 3*r], 0)
	ellipse(screen, BLACK, [x, y, 6*r, 3*r], 1)
	# mouth
	ellipse(screen, BLACK, [x+3*r, y+2*r, (5*r)//2, 10], 1)
	rect(screen, WHITE, [x+3*r, y+2*r, (5*r)//2, 5], 0)
	#eyes
	circle(screen, BLACK, (x+5*r, y+r), 5, 0)
	circle(screen, BLACK, (x+3*r+r//2, y+r), 5, 0)
	#ear
	#circle(screen, WHITE, (x+25, y+15), 15, 0)
	#circle(screen, BLACK, (x+25, y+15), 15, 1)
	#rect(screen, WHITE, [x+20, y+10, 25, 20], 0)
	draw_ear(x+r, y+(3*r)//5, (3*r)//5)



def draw_bear(x=20, y=400, r=25):

	#draw_head(x+90, y-60)
	
	draw_head_2(x+75, y-50, 25)
	
	#body
	ellipse(screen, WHITE, [x, y, 8*r, 16*r], 0)
	ellipse(screen, BLACK, [x, y, 8*r, 16*r], 1)
	
	draw_hole(x+19*r, y+12*r, 2*r)
	
	#fishing rod
	line(screen, BLACK, (x+8*r+r//2, y+7*r), (x+18*r+r//2, y-3*r), 5)
	line(screen, BLACK, (x+18*r, y-3*r+r//2), (x+18*r, y+12*r), 1)
	
	#line(screen, BLACK, (x+200, y+200), (x+475, y-75), 5)
	#line(screen, BLACK, (x+460, y-70), (x+460, y+300), 1)
	
	#hand
	ellipse(screen, WHITE, [x+6*r, y+4*r, 5*r, 2*r], 0)
	ellipse(screen, BLACK, [x+6*r, y+4*r, 5*r, 2*r], 1)
	
	#leg
	ellipse(screen, WHITE, [x+4*r, y+12*r, 6*r, 4*r], 0)
	ellipse(screen, BLACK, [x+4*r, y+12*r, 6*r, 4*r], 1)
	ellipse(screen, WHITE, [x+8*r+r//2, y+14*r, 3*r, 2*r], 0)
	ellipse(screen, BLACK, [x+8*r+r//2, y+14*r, 3*r, 2*r], 1)



pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 900))

#sky
rect(screen, SKY, (0, 0, 700, 450))
rect(screen, WHITE, (0, 450, 700, 450))
line(screen, BLACK, (0, 450), (700, 450), 1)

#sun
draw_sun(500, 200, 190)

'''#head
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
ellipse(screen, BLACK, [235, 750, 75, 50], 1)'''

draw_bear()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.time.get_ticks() > 5000):
            finished = True

pygame.quit()
