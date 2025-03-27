import pygame as py
import time
import random
import sys
import math

py.init()

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
headpat = False
default = True #in use
blink = False #in use
glitch = False
startup = False
ouch = False
#actions
mousefollowing = False
sleepytimer = 0
timerforrainbow = 0
typergb = ""
#colors
red = int(127.5 * (math.sin(timerforrainbow) + 1))
green = int(127.5 * (math.sin(timerforrainbow + 2 * math.pi / 3) + 1))
blue = int(127.5 * (math.sin(timerforrainbow + 4 * math.pi / 3) + 1))
faceColor = (255, 255, 255)
faceColorBack = (red, green, blue)

while running:
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
    screen.fill((0, 0, 0))
    if (random.randint(0, 7000)) == 1:
        blink = True
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_r or event.key == py.K_g or event.key == py.K_b:
                typergb += event.unicode
            if event.key == py.K_BACKSPACE:
                typergb = ""
    if typergb == "rgb":
        rainbow = not rainbow
        typergb = ""
    # print(str(red) + " " + str(green) + " " + str(blue))
    if blink:                                              #*JUST BLINK
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