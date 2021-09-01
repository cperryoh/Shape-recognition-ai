import pygame, sys
import tensorflow as tf

white = [255, 255, 255]
black = [0, 0, 0]


def getPixelLocation(xpos, ypos, pixelsize):
    x = truncate((xpos / pixelsize) + 1)
    y = truncate((ypos / pixelsize) + 1)
    return int(x), int(y)


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def fillSquare(x, y, fill, screen, pixelSize, data):
    color = black if fill == True else white
    xpos, ypos = getPixelLocation(x, y,pixelSize)
    rect = pygame.draw.rect(screen, color, (x, y, pixelSize, pixelSize), False)
    data[xpos][ypos] = int(0 if fill==False else 1)
def clearallData(data,screen,pixelSize,res):
    for x in range(res):
        for y in range(res):
            xpos=(pixelSize/2)+x*pixelSize
            ypos=(pixelSize/2)+y*pixelSize
            fillSquare(x=xpos,y=ypos,screen=screen,pixelSize=pixelSize,data=data,fill=False)
def drawShape(_res, size,cap):
    res = _res
    pixelsize = size
    screen_size = res * pixelsize
    pixeldata = arr = [[0 for i in range(res)] for j in range(res)]
    for x in range(0, res - 1):
        for y in range(0, res - 1):
            pixeldata[x][y] = 0
    going = True
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption(cap)
    screen.fill(white)
    pygame.display.flip()
    lastx=0
    lasty=0
    while going:
        pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("enter")
                    return pixeldata;
                if event.key == pygame.K_END:
                    clearallData(data=pixeldata,screen=screen,pixelSize=pixelsize,res=res)

        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and(x!=lastx and y!=lasty):
            lastx=x
            lasty=y
            x, y = pygame.mouse.get_pos()
            xpos, ypos = getPixelLocation(x, y,pixelsize)
            # get a list of all sprites that are under the mouse cursor
            fill = True
            fillSquare((xpos * pixelsize) - pixelsize, (ypos * pixelsize) - pixelsize, fill, screen,pixelsize, pixeldata)
            # do something with the clicked sprites...
        if pygame.mouse.get_pressed()[2] and(x!=lastx and y!=lasty):
            lastx=x
            lasty=y
            x, y = pygame.mouse.get_pos()
            xpos, ypos = getPixelLocation(x, y,pixelsize)
            # get a list of all sprites that are under the mouse cursor
            fill = False
            fillSquare((xpos * pixelsize) - pixelsize, (ypos * pixelsize) - pixelsize, fill, screen,pixelsize, pixeldata)
            # do something with the clicked sprites...
        pygame.display.update()
