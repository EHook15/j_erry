import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))

clock = pygame.time.Clock()
running = True
#colors
faceColor = (201, 246, 255)
faceColorBack = (77, 224, 255)
#linewidth
facewidth = 5
backfacewidth = 15
#emotion
smile = False
happy = False
sad = False
uwu = False
sleepy = False
headpat = False
default = True #in use
glitch = False
startup = False
#def emotions

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if default:
        #points for polygons
        a = (122, 0)
        b = (0, 0)
        c = (0, 0)
        d = (0, 0)
        e = (0, 0)
        f = (0, 0)
        g = (0, 0)
        h = (0, 0)
        i = (0, 0)
        j = (0, 0)
        k = (0, 0)
        l = (0, 0)
        pygame.draw.polygon(screen, faceColorBack, [a, b, c, d], backfacewidth) #eye 1 back
        pygame.draw.polygon(screen, faceColorBack, [e, f, g ,h], backfacewidth) #eye 2 back
        pygame.draw.polygon(screen, faceColorBack, [i, j, k, l], backfacewidth) #mouth back
        pygame.draw.polygon(screen, faceColor, [a, b, c, d], facewidth) #eye 1
        pygame.draw.polygon(screen, faceColor, [e, f, g ,h], facewidth) #eye 2
        pygame.draw.polygon(screen, faceColor, [i, j, k, l], facewidth) #mouth
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()