import pygame
import time
from pygame.draw import *
from random import randint

print("Enter your name: ")
name = input()
i = 0
while i < len(name): #Percent symbols are banned
	if name[i] == '%':
		name = name[:i] + name[i+1:]
		continue
	i+=1

pygame.init()

FPS = 20
BPS = 1.5 #balls to appear per second
SPS = 30 #seconds for special target to appear
LIFETIME = 20 #a lifetime of a ball, seconds
LIFETIME_S = 2 #a lifetime of a target, seconds
WIDTH = 1200
HEIGHT = 900
MAX_SPEED = 200 #maximum ball speed, px/second
STOP = True #if false, game will run infinitely

screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]
arial = pygame.font.SysFont("Arial Black", 64)
PATH = 'score.txt' #Where we will save our score

def new_ball(time):
	#creates new ball
	x = randint(100, WIDTH-100)
	y = randint(100, HEIGHT-100)
	r = randint(10, 100)
	dx = randint(-MAX_SPEED, MAX_SPEED)
	dy = randint(-MAX_SPEED, MAX_SPEED)
	color = COLORS[randint(0, 6)]
	if color == WHITE:
		color = (randint(0, 255), randint(0, 255), randint(0, 255))
	return([x, y, r, color, time, dx, dy])


def special_create():
	#creates a special target
	x = randint(100, WIDTH-100)
	y = randint(100, HEIGHT-100)
	r = 3*randint(15, 40)
	return([x, y, r, r])


def draw_special(x, y, r):
	polygon(screen, WHITE, [(x-r, y), (x, y-r), (x+r, y), (x, y+r)])
	polygon(screen, RED, [(x-(2*r)//3, y), (x, y-(2*r)//3), (x+(2*r)//3, y), (x, y+(2*r)//3)])
	polygon(screen, BLACK, [(x-r//3, y), (x, y-r//3), (x+r//3, y), (x, y+r//3)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
score2 = 0
special_score = 0
badscore = 0
special = False

ball_list = []
ball_count = 0 #number of balls
littleclock = 0 #this will count up, when equals /period/, a new ball will appear
period = int(FPS/BPS)
GAMEOVER = False

while not finished:
	clock.tick(FPS)
	clicked = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x,y = event.pos
			for ball in ball_list:
				if ((not clicked) and ((x-ball[0])**2 + (y-ball[1])**2 <= ball[2]**2)):
					score += 100//ball[2] #score for size
					score2 += int(((ball[5]**2 + ball[6]**2)**0.5)/100) #score for speed
					clicked = True
					ball[4] = 0 #remove the ball we clicked on
					break
			if ((not clicked) and special and (abs(x-target[0]) + abs(y - target[1]) <= target[2])):
				special_score+=10
				special = False
			elif not clicked:
				badscore+=1

	screen.fill(BLACK)
	
	to_murder = -1 #number of the ball to eliminate
	i = 0
	for ball in ball_list:
		ball[0]+=ball[5]/FPS #ball movement
		ball[1]+=ball[6]/FPS

		if ((ball[0] < ball[2]) or (ball[0] > WIDTH-ball[2])): #ball reflection
			ball[5] = -ball[5]
		if ((ball[1] < ball[2]) or (ball[1] > HEIGHT-ball[2])):
			ball[6] = -ball[6]

		circle(screen, ball[3], (int(ball[0]), int(ball[1])), ball[2]) #redrawing ball

		ball[4] -= 1 #ball lifetime countdown
		if ball[4] <= 0:
			to_murder = i
		i+=1
	if to_murder >= 0:
		ball_list.pop(to_murder) #ball dies
		ball_count -= 1

	if special: #special target draws itself & shrinks
		if int(target[2]) <= 0:
			special = False
		draw_special(target[0], target[1], int(target[2]))
		target[2] -= target[3]/(FPS*LIFETIME_S)
	
	if (littleclock%period == 0):
		ball_list.append(new_ball(FPS*LIFETIME)) #a new ball is born
		ball_count += 1

	if ((littleclock%(SPS*FPS) == 0) and (littleclock > 0)): #special target is born
		target = special_create()
		special = True

	#printing scores
	text = arial.render(str(score), True, WHITE)
	screen.blit(text, (20, 20))

	text2 = arial.render(str(score2), True, WHITE)
	screen.blit(text2, (120, 20))
	
	special_text = arial.render(str(special_score), True, GREEN)
	screen.blit(special_text, (1040, 20))
	
	if badscore>0:
		text3 = arial.render(str(badscore), True, RED)
		screen.blit(text3, (1140, 20))

	#printing ball count
	if ball_count < 5:
		num_color = WHITE
	elif ball_count < 10:
		num_color = GREEN
	elif ball_count < 15:
		num_color = YELLOW
	else:
		num_color = RED
	text_num = arial.render(str(ball_count), True, num_color)
	screen.blit(text_num, (220, 20))

	pygame.display.update()

	littleclock+=1

	if ((badscore>=10) or (ball_count>=15)):
		GAMEOVER = True

	if (GAMEOVER and STOP):
		break

pygame.quit()

#And now it's time to save our results.
gametime = time.ctime(time.time())
summary = score + score2 + special_score
desc = '(' + str(score) + ' points in Size, ' + str(score2) + ' points in Speed, ' + str(special_score) + ' special points)'
new_line = str(summary) + ' % ' + desc + ' % ' + name + ' % ' + gametime + '\n'

f = open(PATH, 'r')
lines = []
for line in f:
	literals = []
	for i in range(len(line)):
		if line[i] == '%':
			literals.append(i)
	line2 = [int(line[:literals[0]-1]), line[literals[0]+2:literals[1]-1], line[literals[1]+2:literals[2]-1], line[literals[2]+2:]]
	lines.append(line2)
f.close()

g = open(PATH, 'w')
written = False
i = 0
while i < len(lines):
	line = lines[i]
	to_write = str(line[0]) + ' % ' + line[1] + ' % ' + line[2] + ' % ' + line[3]
	if ((not written) and (line[0]<=summary)):
		written = True
		g.write(new_line)
		continue
	g.write(to_write)
	i+=1
if (not written):
		written = True
		g.write(new_line)
g.close()


