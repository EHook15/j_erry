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
headpat = False #headpat
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
    if headpat:                                                  #HEADPAT
        screen.fill((0, 0, 0))
        #points for polygons
        a = (125, 148)
        b = (185, 135)
        c = (178, 185)
        d = (129, 193)
        e = (252, 125)
        f = (307, 128)
        g = (306, 191)
        h = (253, 185)
        i = (77, 226)
        j = (61, 264)
        k = (378, 260)
        l = (358, 211)
        m = (71, 180) 
        n = (38, 197)
        o = (90, 200)
        p = (57, 219)
        q = (340, 164)
        r = (378, 180)
        s = (327, 185)
        t = (364, 200)
        pygame.draw.line(screen, faceColorBack, d, a, backfacewidth) #eye 1 back pet
        pygame.draw.line(screen, faceColorBack, a, b, backfacewidth)
        pygame.draw.line(screen, faceColorBack, b, c, backfacewidth)
        pygame.draw.line(screen, faceColorBack, h, e, backfacewidth) #eye 2 back pet
        pygame.draw.line(screen, faceColorBack, e, f, backfacewidth)
        pygame.draw.line(screen, faceColorBack, f, g, backfacewidth)
        pygame.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        pygame.draw.line(screen, faceColorBack, j, k, backfacewidth)
        pygame.draw.line(screen, faceColorBack, k, l, backfacewidth)
        pygame.draw.line(screen, faceColor, d, a, facewidth) #eye 1 pet
        pygame.draw.line(screen, faceColor, a, b, facewidth)
        pygame.draw.line(screen, faceColor, b, c, facewidth)
        pygame.draw.line(screen, faceColor, h, e, facewidth) #eye 2 pet
        pygame.draw.line(screen, faceColor, e, f, facewidth)
        pygame.draw.line(screen, faceColor, f, g, facewidth)
        pygame.draw.line(screen, faceColor, i, j, facewidth) #mouth
        pygame.draw.line(screen, faceColor, j, k, facewidth)
        pygame.draw.line(screen, faceColor, k, l, facewidth)
        pygame.draw.line(screen, faceColorBack, m, n, 10) #blush back
        pygame.draw.line(screen, faceColorBack, o, p, 10)
        pygame.draw.line(screen, faceColorBack, q, r, 10)
        pygame.draw.line(screen, faceColorBack, s, t, 10)
        pygame.draw.line(screen, faceColor, m, n, 3) #blush
        pygame.draw.line(screen, faceColor, o, p, 3)
        pygame.draw.line(screen, faceColor, q, r, 3)
        pygame.draw.line(screen, faceColor, s, t, 3)
        pygame.display.flip()
        headpat = False
        blink = False
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