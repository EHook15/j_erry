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
startup = True #working on
ouch = False #in use
#actions
mousefollowing = False
sleepytimer = 0
timerforrainbow = 0
typergb = ""
ouchnum = 0
startupoffset = 0
#colors
red = int(127.5 * (math.sin(timerforrainbow) + 1))
green = int(127.5 * (math.sin(timerforrainbow + 2 * math.pi / 3) + 1))
blue = int(127.5 * (math.sin(timerforrainbow + 4 * math.pi / 3) + 1))
faceColor = (255, 255, 255)
faceColorBack = (red, green, blue)
#font for ouch
textboxrect = py.Rect(10, 10, 200, 32)
textouch = ""
#font for startup
textstartup = "Starting j_erry..."

faceColor = (201, 246, 255)
faceColorBack = (30, 224, 255)
while startup:                                         #STARTUP NOT DONE
    for event in py.event.get():
        if event.type == py.QUIT:
            startup = False
            running = False
    startupoffset += 0.05
    screen.fill((0, 0, 0))
    #points for polygons
    startupboxtop = [(0, 200 - startupoffset), (400, 200 - startupoffset), (400, 0), (0, 0)]   #increment with startupoffset
    startupboxtophighlight = [(0, 200 - startupoffset), (400, 200 - startupoffset)]
    startupboxbottom = [(0, 200 + startupoffset), (400, 200 + startupoffset), (400, 400), (0, 400)]
    startupboxbottomhighlight = [(0, 200 + startupoffset), (400, 200 + startupoffset)]
    eye1 = [(125, 128), (185, 115), (178, 220), (129, 222)]
    eye2 = [(252, 105), (307, 108), (306, 216), (253, 220)]
    mouth = [(77, 246), (61, 284), (378, 270), (358, 211)]
    py.draw.polygon(screen, faceColorBack, eye1, backfacewidth) #eye 1 back
    py.draw.polygon(screen, faceColorBack, eye2, backfacewidth) #eye 2 back
    py.draw.lines(screen, faceColorBack, False, mouth, backfacewidth) #mouth back
    py.draw.polygon(screen, faceColor, eye1, facewidth) #eye 1
    py.draw.polygon(screen, faceColor, eye2, facewidth) #eye 2
    py.draw.lines(screen, faceColor, False, mouth, facewidth) #mouth
    py.draw.polygon(screen, (0, 0, 0), startupboxtop) #startupboxtop
    py.draw.polygon(screen, (0, 0, 0), startupboxbottom) #startupboxbottom
    if startupoffset <= 154:
        py.draw.rect(screen, (0, 0, 0), textboxrect)
        textsurface = font.render(textstartup, True, (0, 255, 255))
        screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
    py.draw.lines(screen, faceColorBack, True, startupboxtophighlight, 25) #startupboxtophighlight back
    py.draw.lines(screen, faceColorBack, True, startupboxbottomhighlight, 25) #startupboxbottomhighlight back
    py.draw.lines(screen, faceColor, True, startupboxtophighlight, 8) #startupboxtophighlight front
    py.draw.lines(screen, faceColor, True, startupboxbottomhighlight, 8) #startupboxbottomhighlight front
    if startupoffset >= 200:
        blink = True
        startup = False
    py.display.flip()

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
    if mousey < 100 and mousex > 100 and mousex < 300 and mousexrel != 0 or mouseyrel != 0:
        timerforheadpat += 1
    if timerforheadpat >= 150:
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
    if ouch:                                                 #OUCH
        faceColor = (250, 230, 230)
        faceColorBack = (170, 0, 0)
        screen.fill((0, 0, 0))
        #points for polygons
        eye1 = [(125, 108), (306, 216)]
        eye2 = [(306, 108), (129, 222)]
        mouth = [(228, 270), (221, 284)]
        py.draw.lines(screen, faceColorBack, True, eye1, backfacewidth) #eye line 1 back
        py.draw.lines(screen, faceColorBack, True, eye2, backfacewidth) #eye line 2 back
        py.draw.lines(screen, faceColorBack, False, mouth, backfacewidth) #mouth back
        py.draw.lines(screen, faceColor, True, eye1, facewidth) #eye line 1
        py.draw.lines(screen, faceColor, True, eye2, facewidth) #eye line 2
        py.draw.lines(screen, faceColor, False, mouth, facewidth) #mouth
        py.draw.rect(screen, (0, 0, 0), textboxrect)
        textsurface = font.render(textouch, True, (255, 0, 0))
        screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
        py.display.flip()
        ouch = False
        time.sleep(0.5)
    elif headpat:                                            #HEADPAT
        screen.fill((0, 0, 0))
        sleepytimer = 0
        #points for polygons
        eye1 = [(129, 193), (125, 148), (185, 135), (178, 185)]
        eye2 = [(253, 185), (252, 125), (307, 128), (306, 191)]
        mouth = [(77, 226), (61, 264), (378, 260), (358, 211)]
        blush1 = [(71, 180), (38, 197)]
        blush2 = [(90, 200), (57, 219)]
        blush3 = [(340, 164), (378, 180)]
        blush4 = [(327, 185), (364, 200)]
        py.draw.lines(screen, faceColorBack, False, eye1, backfacewidth) #eye1pet back
        py.draw.lines(screen, faceColorBack, False, eye2, backfacewidth) #eye2pet back
        py.draw.lines(screen, faceColorBack, False, mouth, backfacewidth) #mouth back
        py.draw.lines(screen, faceColorBack, False, blush1, 10) #blush1 back
        py.draw.lines(screen, faceColorBack, False, blush2, 10) #blush2 back
        py.draw.lines(screen, faceColorBack, False, blush3, 10) #blush3 back
        py.draw.lines(screen, faceColorBack, False, blush4, 10) #blush4 back
        py.draw.lines(screen, faceColor, False, eye1, facewidth) #eye1pet
        py.draw.lines(screen, faceColor, False, eye2, facewidth) #eye2pet
        py.draw.lines(screen, faceColor, False, mouth, facewidth) #mouth
        py.draw.lines(screen, faceColor, False, blush1, 3) #blush1
        py.draw.lines(screen, faceColor, False, blush2, 3) #blush2
        py.draw.lines(screen, faceColor, False, blush3, 3) #blush3
        py.draw.lines(screen, faceColor, False, blush4, 3) #blush4
        headpat = False
        ouchnum -= 1
        textouch = textouch[:-3]
        py.draw.rect(screen, (0, 0, 0), textboxrect)
        textsurface = font.render(textouch, True, (255, 0, 0))
        screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
        py.display.flip()
        time.sleep(1)
    elif blink:                                              #JUST BLINK
        screen.fill((0, 0, 0))
        #points for polygons
        blinkline = [(90, 200), (218, 210), (330, 190)]
        mouth = [(77, 246), (61, 284), (378, 270), (358, 211)]
        py.draw.lines(screen, faceColorBack, False, blinkline, backfacewidth) #blink line back
        py.draw.lines(screen, faceColorBack, False, mouth, backfacewidth) #mouth back
        py.draw.lines(screen, faceColor, False, blinkline, facewidth) #blink line
        py.draw.lines(screen, faceColor, False, mouth, facewidth) #mouth
        py.draw.rect(screen, (0, 0, 0), textboxrect)
        textsurface = font.render(textouch, True, (255, 0, 0))
        screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
        screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
        py.display.flip()
        blink = False
        time.sleep(0.2)
    elif default:                                            #DEFAULT
        screen.fill((0, 0, 0))
        #points for polygons
        eye1 = [(125, 128), (185, 115), (178, 220), (129, 222)]
        eye2 = [(252, 105), (307, 108), (306, 216), (253, 220)]
        mouth = [(77, 246), (61, 284), (378, 270), (358, 211)]
        py.draw.polygon(screen, faceColorBack, eye1, backfacewidth) #eye 1 back
        py.draw.polygon(screen, faceColorBack, eye2, backfacewidth) #eye 2 back
        py.draw.lines(screen, faceColorBack, False, mouth, backfacewidth) #mouth back
        py.draw.polygon(screen, faceColor, eye1, facewidth) #eye 1
        py.draw.polygon(screen, faceColor, eye2, facewidth) #eye 2
        py.draw.lines(screen, faceColor, False, mouth, facewidth) #mouth
        py.draw.rect(screen, (0, 0, 0), textboxrect)
        textsurface = font.render(textouch, True, (255, 0, 0))
        screen.blit(textsurface, (textboxrect.x + 5, textboxrect.y + 5))
        py.display.flip()
    py.display.flip()
py.quit()