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
blink = False #in use
glitch = False
startup = False
ouch = False

while running:
    mousex, mousey = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if mousey < 100 and mousex > 100 and mousex < 300:
        headpat = True
    if (random.randint(0, 10000) == 1):
        blink = True
    if blink and headpat:                                        #BLINK AND HEADPAT
        screen.fill((0, 0, 0))
        a = (90, 200)
        b = (218, 210)
        c = (330, 190)
        i = (77, 246)
        j = (61, 284)
        k = (378, 270)
        l = (358, 211)
        pygame.draw.line(screen, faceColorBack, a, b, backfacewidth) #blink line back
        pygame.draw.line(screen, faceColorBack, b, c, backfacewidth)
        pygame.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        pygame.draw.line(screen, faceColorBack, j, k, backfacewidth)
        pygame.draw.line(screen, faceColorBack, k, l, backfacewidth)
        pygame.draw.line(screen, faceColor, a, b, facewidth) #blink line
        pygame.draw.line(screen, faceColor, b, c, facewidth)
        pygame.draw.line(screen, faceColor, i, j, facewidth) #mouth
        pygame.draw.line(screen, faceColor, j, k, facewidth)
        pygame.draw.line(screen, faceColor, k, l, facewidth)
        pygame.display.flip()
        if random.randint(0, 1) == 1:
            time.sleep(0.4)
        else:
            time.sleep(0.2)
        blink = False
        headpat = False
    elif headpat:                                                  #HEADPAT
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
        headpat = False
    elif blink:                                                    #JUST BLINK
        screen.fill((0, 0, 0))
        #points for polygons
        a = (90, 200)
        b = (218, 210)
        c = (330, 190)
        i = (77, 246)
        j = (61, 284)
        k = (378, 270)
        l = (358, 211)
        pygame.draw.line(screen, faceColorBack, a, b, backfacewidth) #blink line back
        pygame.draw.line(screen, faceColorBack, b, c, backfacewidth)
        pygame.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        pygame.draw.line(screen, faceColorBack, j, k, backfacewidth)
        pygame.draw.line(screen, faceColorBack, k, l, backfacewidth)
        pygame.draw.line(screen, faceColor, a, b, facewidth) #blink line
        pygame.draw.line(screen, faceColor, b, c, facewidth)
        pygame.draw.line(screen, faceColor, i, j, facewidth) #mouth
        pygame.draw.line(screen, faceColor, j, k, facewidth)
        pygame.draw.line(screen, faceColor, k, l, facewidth)
        pygame.display.flip()
        if random.randint(0, 1) == 1:
            time.sleep(0.4)
        else:
            time.sleep(0.2)
        blink = False
    elif default:                                                 #DEFAULT
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
    pygame.display.flip()

pygame.quit()