import pygame
import time
import random
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))

running = True
timerforheadpat = 0
#colors
faceColor = (201, 246, 255)
faceColorBack = (77, 224, 255)
#linewidth
facewidth = 5
backfacewidth = 15
#emotion
rainbow = False
happy = False
sad = False
uwu = False #in use
sleepy = False 
headpat = False #in use
default = True #in use
blink = False #in use
glitch = False
startup = False
ouch = False
#actions
mousefollowing = False
typeuwu = ""
sleepytimer = 0

while running:
    mousex, mousey = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    sleepytimer += 1
    print(sleepytimer)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: 
                mousefollowing = not mousefollowing
            elif event.type == pygame.K_u or pygame.K_w:
                typeuwu += event.unicode
            if event.type == pygame.K_BACKSPACE:
                typeuwu = ""
            if typeuwu.lower() == "uwu":
                uwu = not uwu
                typeuwu = ""
    if mousey < 100 and mousex > 100 and mousex < 300:
        timerforheadpat += 1
    else:
        timerforheadpat = 0
    if timerforheadpat >= 1500:
        sleepy = False
        headpat = True
        timerforheadpat = 0
    if (random.randint(0, 10000) == 1):
        blink = True
    if sleepytimer >= 3000:
        sleepy = True
    if sleepy:                                                    #!SLEEPY not done and (needs uwu)
        screen.fill((0, 0, 0))
        #points for polygons
        a = (125, 128)
        b = (185, 115)
        i = (77, 246)
        j = (61, 284)
        k = (378, 270)
        l = (358, 211)
        u = (64, 127)
        v = (90, 24)
        w = (163, 76)
        x = (260, 75)
        y = (340, 21)
        z = (352, 113)
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
    elif mousefollowing and blink:                                #*MOUSEFOLLOW AND BLINK
        sleepytimer = 0
        screen.fill((0, 0, 0))
        offsetx = (mousex / 4) - 80
        offsety = (mousey / 4) - 80
        #points for polygons
        a = (90 + offsetx, 200 + offsety)
        b = (218 + offsetx, 210 + offsety)
        c = (330 + offsetx, 190 + offsety)
        i = (77 + offsetx / 2, 246 + offsety / 1)
        j = (61 + offsetx / 2, 284 + offsety / 1)
        k = (378 + offsetx / 2, 270 + offsety / 3)
        l = (358 + offsetx / 2, 211 + offsety / 3)
        u = (64 + offsetx / 2, 127 + offsety / 3)
        v = (90 + offsetx / 2, 24 + offsety / 3)
        w = (163 + offsetx / 2, 76 + offsety / 3)
        x = (260 + offsetx / 2, 75 + offsety / 3)
        y = (340 + offsetx / 2, 21 + offsety / 3)
        z = (352 + offsetx / 2, 113 + offsety / 3)
        if uwu:
            pygame.draw.line(screen, faceColorBack, u, v, backfacewidth)      #TODO: FIX
            pygame.draw.line(screen, faceColorBack, v, w, backfacewidth)
            pygame.draw.line(screen, faceColorBack, x, y, backfacewidth)
            pygame.draw.line(screen, faceColorBack, y, z, backfacewidth)
            pygame.draw.line(screen, faceColor, u, v, facewidth)
            pygame.draw.line(screen, faceColor, v, w, facewidth)
            pygame.draw.line(screen, faceColor, x, y, facewidth)
            pygame.draw.line(screen, faceColor, y, z, facewidth)
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
    elif mousefollowing:                                          #*JUST MOUSEFOLLOW
        sleepytimer = 0
        screen.fill((0, 0, 0))
        offsetx = (mousex / 4) - 80
        offsety = (mousey / 4) - 80
        #points for polygons
        a = (125 + offsetx, 128 + offsety)
        b = (185 + offsetx, 115 + offsety)
        c = (178 + offsetx, 220 + offsety)
        d = (129 + offsetx, 222 + offsety)
        e = (252 + offsetx, 105 + offsety)
        f = (307 + offsetx, 108 + offsety)
        g = (306 + offsetx, 216 + offsety)
        h = (253 + offsetx, 220 + offsety)
        i = (77 + offsetx / 2, 246 + offsety / 1)
        j = (61 + offsetx / 2, 284 + offsety / 1)
        k = (378 + offsetx / 2, 270 + offsety / 3)
        l = (358 + offsetx / 2, 211 + offsety / 3)
        u = (64 + offsetx / 2, 127 + offsety / 3)
        v = (90 + offsetx / 2, 24 + offsety / 3)
        w = (163 + offsetx / 2, 76 + offsety / 3)
        x = (260 + offsetx / 2, 75 + offsety / 3)
        y = (340 + offsetx / 2, 21 + offsety / 3)
        z = (352 + offsetx / 2, 113 + offsety / 3)
        if uwu:
            pygame.draw.line(screen, faceColorBack, u, v, backfacewidth)      #TODO: FIX
            pygame.draw.line(screen, faceColorBack, v, w, backfacewidth)
            pygame.draw.line(screen, faceColorBack, x, y, backfacewidth)
            pygame.draw.line(screen, faceColorBack, y, z, backfacewidth)
            pygame.draw.line(screen, faceColor, u, v, facewidth)
            pygame.draw.line(screen, faceColor, v, w, facewidth)
            pygame.draw.line(screen, faceColor, x, y, facewidth)
            pygame.draw.line(screen, faceColor, y, z, facewidth)
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
    elif headpat:                                                  #*HEADPAT
        screen.fill((0, 0, 0))
        sleepytimer = 0
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
        u = (64, 127)
        v = (90, 24)
        w = (163, 76)
        x = (260, 75)
        y = (340, 21)
        z = (352, 113)
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
        if uwu:                                                 #TODO: make the ears move when pet
            pygame.draw.line(screen, faceColorBack, u, v, backfacewidth)
            pygame.draw.line(screen, faceColorBack, v, w, backfacewidth)
            pygame.draw.line(screen, faceColorBack, x, y, backfacewidth)
            pygame.draw.line(screen, faceColorBack, y, z, backfacewidth)
            pygame.draw.line(screen, faceColor, u, v, facewidth)
            pygame.draw.line(screen, faceColor, v, w, facewidth)
            pygame.draw.line(screen, faceColor, x, y, facewidth)
            pygame.draw.line(screen, faceColor, y, z, facewidth)
        pygame.display.flip()
        time.sleep(1)
        headpat = False
        blink = False
    elif blink:                                                    #*JUST BLINK
        screen.fill((0, 0, 0))
        #points for polygons
        a = (90, 200)
        b = (218, 210)
        c = (330, 190)
        i = (77, 246)
        j = (61, 284)
        k = (378, 270)
        l = (358, 211)
        u = (64, 127)
        v = (90, 24)
        w = (163, 76)
        x = (260, 75)
        y = (340, 21)
        z = (352, 113)
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
        if uwu:
            pygame.draw.line(screen, faceColorBack, u, v, backfacewidth)
            pygame.draw.line(screen, faceColorBack, v, w, backfacewidth)
            pygame.draw.line(screen, faceColorBack, x, y, backfacewidth)
            pygame.draw.line(screen, faceColorBack, y, z, backfacewidth)
            pygame.draw.line(screen, faceColor, u, v, facewidth)
            pygame.draw.line(screen, faceColor, v, w, facewidth)
            pygame.draw.line(screen, faceColor, x, y, facewidth)
            pygame.draw.line(screen, faceColor, y, z, facewidth)
        pygame.display.flip()
        if random.randint(0, 1) == 1:
            time.sleep(0.4)
        else:
            time.sleep(0.2)
        blink = False
    elif default:                                                 #*DEFAULT
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
        u = (64, 127)
        v = (90, 24)
        w = (163, 76)
        x = (260, 75)
        y = (340, 21)
        z = (352, 113)
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
        if uwu:
            pygame.draw.line(screen, faceColorBack, u, v, backfacewidth)
            pygame.draw.line(screen, faceColorBack, v, w, backfacewidth)
            pygame.draw.line(screen, faceColorBack, x, y, backfacewidth)
            pygame.draw.line(screen, faceColorBack, y, z, backfacewidth)
            pygame.draw.line(screen, faceColor, u, v, facewidth)
            pygame.draw.line(screen, faceColor, v, w, facewidth)
            pygame.draw.line(screen, faceColor, x, y, facewidth)
            pygame.draw.line(screen, faceColor, y, z, facewidth)
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()