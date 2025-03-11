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
        a = (125, 128)
        b = (185, 115)
        c = (178, 220)
        d = (129, 222)
        e = (252, 105)
        f = (307, 108)
        g = (306, 216)
        h = (253, 220)
        i = (77, 246)
        j = (41, 284)
        k = (378, 270)
        l = (358, 211)
        pygame.draw.polygon(screen, faceColorBack, [a, b, c, d], backfacewidth) #eye 1 back
        pygame.draw.polygon(screen, faceColorBack, [e, f, g ,h], backfacewidth) #eye 2 back
        pygame.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        pygame.draw.line(screen, faceColorBack, j, k, backfacewidth)
        pygame.draw.line(screen, faceColorBack, k, l, backfacewidth)
        pygame.draw.polygon(screen, faceColor, [a, b, c, d], facewidth) #eye 1
        pygame.draw.polygon(screen, faceColor, [e, f, g ,h], facewidth) #eye 2
        pygame.draw.line(screen, faceColor, i, j, facewidth) #mouth
        pygame.draw.line(screen, faceColor, j, k, facewidth)
        pygame.draw.line(screen, faceColor, k, l, facewidth)
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()