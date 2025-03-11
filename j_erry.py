import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))

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
blink = False
glitch = False
startup = False
ouch = False
#def emotions

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if (random.randint(0, 10) == 1):
        blink = True
    if blink:
        screen.fill((0, 0, 0))
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
        j = (61, 284)
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
        time.sleep(0.1)
        screen.fill((0, 0, 0))
        a = (90, 200)
        b = (330, 190)
        i = (77, 246)
        j = (61, 284)
        k = (378, 270)
        l = (358, 211)
        pygame.draw.line(screen, faceColorBack, a, b, backfacewidth) #blink line back
        pygame.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        pygame.draw.line(screen, faceColorBack, j, k, backfacewidth)
        pygame.draw.line(screen, faceColorBack, k, l, backfacewidth)
        pygame.draw.line(screen, faceColor, a, b, facewidth) #blink line
        pygame.draw.line(screen, faceColor, i, j, facewidth) #mouth
        pygame.draw.line(screen, faceColor, j, k, facewidth)
        pygame.draw.line(screen, faceColor, k, l, facewidth)
        time.sleep(0.5)
        blink = False
    elif default:
        screen.fill((0, 0, 0))
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
        j = (61, 284)
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

pygame.quit()