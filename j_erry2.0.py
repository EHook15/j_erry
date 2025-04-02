import pygame as py
import time
import random
import sys
import math

py.init()
font = py.font.Font(None, 64)

screen = py.display.set_mode((400, 400))

running = True
timerforheadpat = 0
sleepytimer = 0

#linewidth
facewidth = 5
backfacewidth = 15
#emotion
rainbow = False #in use
happy = False
sad = False
sleepy = False
headpat = False #in use
default = True #in use
blink = False #in use
glitch = False
startup = False
ouch = False #in use
#actions
mousefollowing = False
sleepytimer = 0
timerforrainbow = 0
typergb = ""
ouchnum = 0
#colors
red = int(127.5 * (math.sin(timerforrainbow) + 1))
green = int(127.5 * (math.sin(timerforrainbow + 2 * math.pi / 3) + 1))
blue = int(127.5 * (math.sin(timerforrainbow + 4 * math.pi / 3) + 1))
faceColor = (255, 255, 255)
faceColorBack = (red, green, blue)
#font for ouch
textboxrect = py.Rect(10, 10, 200, 32)
textouch = ""

while running:
    py.draw.rect(screen, (0, 0, 0), textboxrect)
    textsurface = font.render(textouch, True, (255, 0, 0))
    screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
    py.display.flip()
    if ouchnum >= 10:                               #if you hurt him 10 times he kills himself
        py.quit()
    if rainbow:
        timerforrainbow += 0.001
        red = int(127.5 * (math.sin(timerforrainbow) + 1))
        green = int(127.5 * (math.sin(timerforrainbow + 2 * math.pi / 3) + 1))
        blue = int(127.5 * (math.sin(timerforrainbow + 4 * math.pi / 3) + 1))
        faceColorBack = (red, green, blue)
        faceColor = (255, 255, 255)
    else:
        faceColor = (201, 246, 255)
        faceColorBack = (30, 224, 255)
    mousex, mousey = py.mouse.get_pos()
    mousexrel, mouseyrel = py.mouse.get_rel()
    if mousey < 100 and mousex > 100 and mousex < 300 and mousexrel !=0 or mouseyrel != 0:
        timerforheadpat += 1
    if timerforheadpat >= 100:
        sleepy = False
        headpat = True
        timerforheadpat = 0
    screen.fill((0, 0, 0))
    if (random.randint(0, 7000)) == 0:
        blink = True
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_r or event.key == py.K_g or event.key == py.K_b:
                typergb += event.unicode
            if event.key == py.K_BACKSPACE:
                typergb = ""
        if event.type == py.MOUSEBUTTONDOWN:
            ouch =  True
            ouchnum += 1
            textouch += " ! "
    if typergb == "rgb":
        rainbow = not rainbow
        typergb = ""
    if ouch:
        faceColor = (250, 230, 230)
        faceColorBack = (170, 0, 0)
        screen.fill((0, 0, 0))
        #points for polygons
        a = (125, 108)
        b = (306, 216)
        c = (306, 108)
        d = (129, 222)
        i = (278, 270)
        j = (161, 284)
        u = (64, 127)
        v = (90, 24)
        w = (163, 76)
        x = (260, 75)
        y = (340, 21)
        z = (352, 113)
        py.draw.line(screen, faceColorBack, a, b, backfacewidth) #eye line 1 back
        py.draw.line(screen, faceColorBack, c, d, backfacewidth) #eye line 2 back
        py.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        py.draw.line(screen, faceColor, a, b, facewidth) #eye line 1
        py.draw.line(screen, faceColor, c, d, facewidth) #eye line 2
        py.draw.line(screen, faceColor, i, j, facewidth) #mouth
        py.draw.rect(screen, (0, 0, 0), textboxrect)
        textsurface = font.render(textouch, True, (255, 0, 0))
        screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
        py.display.flip()
        ouch = False
        time.sleep(0.5)
    elif headpat:                                            #*HEADPAT
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
        py.draw.line(screen, faceColorBack, d, a, backfacewidth) #eye 1 back pet
        py.draw.line(screen, faceColorBack, a, b, backfacewidth)
        py.draw.line(screen, faceColorBack, b, c, backfacewidth)
        py.draw.line(screen, faceColorBack, h, e, backfacewidth) #eye 2 back pet
        py.draw.line(screen, faceColorBack, e, f, backfacewidth)
        py.draw.line(screen, faceColorBack, f, g, backfacewidth)
        py.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        py.draw.line(screen, faceColorBack, j, k, backfacewidth)
        py.draw.line(screen, faceColorBack, k, l, backfacewidth)
        py.draw.line(screen, faceColor, d, a, facewidth) #eye 1 pet
        py.draw.line(screen, faceColor, a, b, facewidth)
        py.draw.line(screen, faceColor, b, c, facewidth)
        py.draw.line(screen, faceColor, h, e, facewidth) #eye 2 pet
        py.draw.line(screen, faceColor, e, f, facewidth)
        py.draw.line(screen, faceColor, f, g, facewidth)
        py.draw.line(screen, faceColor, i, j, facewidth) #mouth
        py.draw.line(screen, faceColor, j, k, facewidth)
        py.draw.line(screen, faceColor, k, l, facewidth)
        py.draw.line(screen, faceColorBack, m, n, 10) #blush back
        py.draw.line(screen, faceColorBack, o, p, 10)
        py.draw.line(screen, faceColorBack, q, r, 10)
        py.draw.line(screen, faceColorBack, s, t, 10)
        py.draw.line(screen, faceColor, m, n, 3) #blush
        py.draw.line(screen, faceColor, o, p, 3)
        py.draw.line(screen, faceColor, q, r, 3)
        py.draw.line(screen, faceColor, s, t, 3)
        headpat = False
        ouchnum -= 1
        textouch = textouch[:-3]
        py.display.flip()
        time.sleep(1)
    elif blink:                                              #*JUST BLINK
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
        py.draw.line(screen, faceColorBack, a, b, backfacewidth) #blink line back
        py.draw.line(screen, faceColorBack, b, c, backfacewidth)
        py.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        py.draw.line(screen, faceColorBack, j, k, backfacewidth)
        py.draw.line(screen, faceColorBack, k, l, backfacewidth)
        py.draw.line(screen, faceColor, a, b, facewidth) #blink line
        py.draw.line(screen, faceColor, b, c, facewidth)
        py.draw.line(screen, faceColor, i, j, facewidth) #mouth
        py.draw.line(screen, faceColor, j, k, facewidth)
        py.draw.line(screen, faceColor, k, l, facewidth)
        py.draw.rect(screen, (0, 0, 0), textboxrect)
        textsurface = font.render(textouch, True, (255, 0, 0))
        screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
        py.display.flip()
        blink = False
        time.sleep(0.2)
    elif default:                                        #*DEFAULT
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
        py.draw.polygon(screen, faceColorBack, [a, b, c, d], backfacewidth) #eye 1 back
        py.draw.polygon(screen, faceColorBack, [e, f, g ,h], backfacewidth) #eye 2 back
        py.draw.line(screen, faceColorBack, i, j, backfacewidth) #mouth back
        py.draw.line(screen, faceColorBack, j, k, backfacewidth)
        py.draw.line(screen, faceColorBack, k, l, backfacewidth)
        py.draw.polygon(screen, faceColor, [a, b, c, d], facewidth) #eye 1
        py.draw.polygon(screen, faceColor, [e, f, g ,h], facewidth) #eye 2
        py.draw.line(screen, faceColor, i, j, facewidth) #mouth
        py.draw.line(screen, faceColor, j, k, facewidth)
        py.draw.line(screen, faceColor, k, l, facewidth)
        py.display.flip()
    py.display.flip()
py.quit()