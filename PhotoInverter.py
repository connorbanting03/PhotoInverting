import pygame
pygame.init()
#Connor Banting 101225905 Assigment7
#If you have any questions please don't hestiate to reach out connorbanting@cmail.carleton.ca
#Have a good one

#Initial Setup
#This could be a function, but mainWindow needs to be within global scope
imageURL = input("Load image url ")
image = pygame.image.load(imageURL)
length, width = image.get_size()
mainWindow = pygame.display.set_mode((length, width))
mainWindow.fill((240, 240, 250))
mainWindow.blit(image, (0, 0))
pygame.display.update()

def inverse(length,width,x,y):
    #This prevents index pixel out of bounds erorrs
    #The edit effect area is a 60x60 pixel roughly but if part of the circle will end up off the edge of the background program will crash
    #This just adjusts the square size
    if(x+30>length):
        xtop=length
    else:
        xtop=x+30
    if(x-30<0):
        xbuttom=0
    else:
        xbuttom=x-30
    if(y+30>width):
        ytop = width
    else:
        ytop = y+30
    if(y-30<0):
        ybottom = 0
    else:
        ybottom = y-30
    #This nested for loop draws the inverted squares, it visits each pixel with the selected area
    #This gets the RGB values, and takes them away from 255 making them inverse colours of each pixel
    for x in range(xbuttom, xtop):
        for y in range(ybottom, ytop):
            (r, g, b, _) = mainWindow.get_at((x, y))

            inverse = (255-r, 255-g, 255-b)

            mainWindow.set_at((x, y), (inverse))



notExit = True
#Active Loop
#First if statement checks if user closes app
#Second one checks for left clicks, and if found gets the cordinates of the click and calls the function to invert the cordinates
while notExit:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            notExit = False
        if pygame.mouse.get_pressed() == (1, 0, 0):
            xvalue, yvalue = pygame.mouse.get_pos()
            inverse(length, width, xvalue, yvalue)
        pygame.display.update()





