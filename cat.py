import pygame,sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsclock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800,650),0,32)
pygame.display.set_caption('Cat Animation')

WHITE = (255,255,255)
catImg = pygame.image.load('123.jpg')
catx=10
caty=10
direction='right'

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx+=0.5
        if catx == 500:
            direction = 'down'
    elif direction == 'down':
        caty+=0.5
        if caty==500:
            direction='left'
    elif direction == 'left':
        catx-=0.5
        if catx==10:
            direction='up'
    elif direction == 'up':
        caty-=0.5
        if caty==10:
            direction = 'right'

DISPLAYSURF.blit(catImg,(catx,caty))
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()        