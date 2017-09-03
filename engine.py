import os 
import sys  
import random 
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
screenWidth = 1000
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.init()
zoom = 10

white = 255,255,255

def randomColour(i):
    red = (i * 7) % 255
    green = (i * 11) % 255
    blue = (i * 13) % 255
    colour = red, green, blue
    return colour

while True:
    screen.fill((0, 0, 0))
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                zoom += 1
            elif event.button == 4 and zoom > 1:
                zoom -= 1
    for i in range(screenWidth/zoom):
        pygame.draw.line(screen, randomColour(i), (i*zoom, 0), (i*zoom, screenHeight))
    for i in range(screenHeight/zoom):
        pygame.draw.line(screen, randomColour(i), (0, i*zoom), (screenWidth, i*zoom))
    pygame.display.flip()
