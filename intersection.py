# Import modules
import sys, pygame, time, math
from time import sleep
from pygame.locals import *
from PIL import Image
import timing
from init import *

# Initialize
maze=('maze6.png')
img = Image.open(maze)
change = 3
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(maze).convert()
newscreen = pygame.transform.scale(background, (width, height))

sleepTime = sleep
#number of turns
upCount = 0
leftCount = 0
rightCount = 0

#Colors
color = (0, 188, 0)
white = (255, 255, 255)
black = (0, 0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

# Recognizing black/white
#-print(width, height)
size = [img.size]
#-print(size[0])
colors = img.getcolors()
#-print(colors)
pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)

xvalueOfStart = list[0] * change
#-print(xvalueOfStart)

blockSize = len(list) * change

yvalueOfStart = height - blockSize

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change
#-print(xvalueOfEnd)

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(sleepTime)

# Function to move forward
def moveUp(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x+1, y - blocksize+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x

# Function to move down
def moveDown(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x+1, y + blocksize+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x   
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize+1, y+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y

# Function to move right
def moveRight(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize+1, y+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y

#Initialization of currentX and currentY
def varsInit(x, y):
    global currentX
    global currentY
    global direction
    currentX = x
    currentY = y
    direction = 1

#Algorithm to determine direction to move if facing up
def up(replace):
    global direction
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("up-Move up called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("up-Move right called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("up-Move left called")
        time.sleep(sleepTime)
        direction = 3
        #check for blue paths
    elif newscreen.get_at((currentX,currentY-blockSize))==blue:
        moveUp(currentX, currentY, blockSize, replace)
        #-print("up-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX+blockSize,currentY))==blue:
        #-print("up-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX-blockSize,currentY))==blue:
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("up-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
        #check rear
    elif newscreen.get_at((currentX, currentY + blockSize)) == white or newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("up-Move down called")
        time.sleep(sleepTime)
        direction = 4
    #-print("direction-up", direction)
    
#Algorithm to determine direction to move if facing right
def right(replace):
    global direction
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("right-Move right called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("right-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("right-Move up called")
        time.sleep(sleepTime)
        direction = 1
    #check blue
    elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("right-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("right-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("right-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    #check rear
    elif newscreen.get_at((currentX - blockSize, currentY)) == white or newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("right-Move left called")
        time.sleep(sleepTime)
        direction = 3
    #-print("direction-right", direction)
    
#Algorithm to determine direction to move if facing left
def left(replace):
    global direction
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("left-Move left called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up
        moveUp(currentX, currentY, blockSize, replace)
        #-print("left-Move up called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down        
        moveDown(currentX, currentY, blockSize, replace)
        #-print("left-Move down called")
        time.sleep(sleepTime)
        direction = 4
        #check blue
    elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("left-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up
        moveUp(currentX, currentY, blockSize, replace)
        #-print("left-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down        
        moveDown(currentX, currentY, blockSize, replace)
        #-print("left-Move down blue called")
        time.sleep(sleepTime)
        direction = 4
        #check rear
    elif newscreen.get_at((currentX + blockSize, currentY)) == white or newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("left-Move right called")
        time.sleep(sleepTime)
        direction = 2
    #-print("direction-left", direction)

#Algorithm to determine direction to move if facing down
def down(replace):
    global direction
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("down-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("down-Move left called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("down-Move right called")
        time.sleep(sleepTime)
        direction = 2
        #check blue
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("down-Move down blue called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("down-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("down-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
        #check rear
    elif newscreen.get_at((currentX, currentY - blockSize)) == white or newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("down-Move up called")
        time.sleep(sleepTime)
        direction = 1
    #-print("direction-down", direction)

#returns boolean if current tile is intersection
def isIntersection():
    global direction
    paths = 0
    #-print("isIntersection")
    if newscreen.get_at((currentX, currentY - blockSize)) == white or newscreen.get_at((currentX, currentY - blockSize)) == red or newscreen.get_at((currentX, currentY - blockSize)) == green or newscreen.get_at((currentX, currentY - blockSize)) == blue:
        paths = paths + 1
        #-print("returnUp")
    if newscreen.get_at((currentX - blockSize, currentY)) == white or newscreen.get_at((currentX - blockSize, currentY)) == red or newscreen.get_at((currentX - blockSize, currentY)) == green or newscreen.get_at((currentX - blockSize, currentY)) == blue:
        paths = paths + 1
        #-print("returnLeft")
    if newscreen.get_at((currentX + blockSize, currentY)) == white or newscreen.get_at((currentX + blockSize, currentY)) == red or newscreen.get_at((currentX + blockSize, currentY)) == green or newscreen.get_at((currentX + blockSize, currentY)) == blue:
        paths = paths + 1
        #-print("returnRight")
    if  newscreen.get_at((currentX, currentY + blockSize)) == white or newscreen.get_at((currentX, currentY + blockSize)) == red or newscreen.get_at((currentX, currentY + blockSize)) == green or newscreen.get_at((currentX, currentY + blockSize)) == blue:
        paths = paths + 1
        #-print("returnDown")
    #-print("direction-isIntersection", direction)
    
    if paths > 2:
        #-print(paths)
        #-print("isIntersection-TRUE")
        return True
    else:
        #-print(paths)
        #-print("isIntersection-FALSE")
        '''
        if direction == 1:
            if(newscreen.get_at((currentX, currentY - blockSize)) == blue):
                moveUp(currentX, currentY, blockSize, white)
            else:
                up(white)
        if direction == 3:
            if(newscreen.get_at((currentX - blockSize, currentY)) == blue):
                moveLeft(currentX, currentY, blockSize, white)
            else:
                left(white)
        if direction == 2:
            if(newscreen.get_at((currentX + blockSize, currentY)) == blue):
                moveRight(currentX, currentY, blockSize, white)
            else:
                right(white)
        if direction == 4:
            if(newscreen.get_at((currentX, currentY + blockSize)) == blue):
                moveUp(currentX, currentY, blockSize, white)
            else:
                down(white)
                '''
        return False

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, white)

'''
1 is up
2 is right
3 is left
4 is down
'''

direction = 1


def checkRed():#returns true if red is present
    global direction
    if newscreen.get_at((currentX, currentY - blockSize)) == red:#up
        direction = 1
        moveUp(currentX, currentY, blockSize, blue)
        return True
    elif newscreen.get_at((currentX + blockSize, currentY)) == red:#right
        direction = 2
        moveRight(currentX, currentY, blockSize, blue)
        return True
    elif newscreen.get_at((currentX - blockSize, currentY)) == red:#left
        direction = 3
        moveLeft(currentX, currentY, blockSize, blue)
        return True
    elif newscreen.get_at((currentX,currentY+blockSize))==red:#down
        direction = 4
        moveDown(currentX, currentY, blockSize, blue)
        return True

    return False
    print("direction-checkRed", direction)

def addCount(isInt,directionMove,firstTime):
    global direction,rightCount,upCount,leftCount
    #direction=direction coming into intersection
    #directionMove=direction leaving intersection
    if isInt:
        print("addCount-isInt")
        if firstTime: #first time at intersection
            print("addCount-first time intersection")
            print("addCount-direction",direction)
            print("addCount-directionMove",directionMove)
            if direction==1:#up
                if directionMove==1:#up
                    upCount+=1
                if directionMove==3:#left
                    leftCount+=1
                if directionMove==2:#right
                    rightCount+=1
            if direction==2:#right
                if directionMove==2:#right
                    upCount+=1
                if directionMove==1:#up
                    leftCount+=1
                if directionMove==4:#down
                    rightCount+=1
            if direction==3:#left
                if directionMove==3:#left
                    upCount+=1
                if directionMove==4:#down
                    leftCount+=1
                if directionMove==1:#up
                    rightCount+=1
            if direction==4:#down
                if directionMove==4:#down
                    upCount+=1
                if directionMove==2:#right
                    leftCount+=1
                if directionMove==3:#left
                    rightCount+=1
                    
        else: #intersection already traveled
            if newscreen.get_at((currentX, currentY - blockSize)) == red:#up-ai faces down
                if direction==4:#ai comes in from bottom-faces up
                    upCount-=1
                if direction==3:#ai comes in from right-faces left
                    leftCount-=1
                if direction==2:#ai comes in from left-faces right
                    rightCount-=1
            elif newscreen.get_at((currentX + blockSize, currentY)) == red:#right-ai faces left
                if direction==2:#ai comes in from left-faces right
                    upCount-=1
                if direction==1:#ai comes in from bottom-faces up
                    leftCount-=1
                if direction==4:#ai comes in from top-faces down
                    rightCount-=1
            elif newscreen.get_at((currentX - blockSize, currentY)) == red:#left-ai faces right
                if direction==3:#ai comes in from right-faces left
                    upCount-=1
                if direction==4:#ai comes in from top-faces down
                    leftCount-=1
                if direction==1:#ai comes in from bottom-faces up
                    rightCount-=1
            elif newscreen.get_at((currentX, currentY + blockSize)) == red:#down-ai faces up
                if direction==4:#ai comes in from top-faces down
                    upCount-=1
                if direction==2:#ai comes in from left-faces right
                    leftCount-=1
                if direction==3:#ai comes in from right-faces left
                    rightCount-=1
                       

    print("directionMove",directionMove)
    print("direction",direction)
    print("RIGHT PATH CHOSEN",rightCount)
    print("LEFT PATH CHOSEN",leftCount)
    print("FRONT PATH CHOSEN",upCount)
    time.sleep(0)
# Check if all paths of an intersection have been travelled. If so, go back on red
def intersection(isInt,firstTime):
    global direction, upCount, rightCount, leftCount
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up
        addCount(isInt,1,firstTime)
        direction = 1
        moveUp(currentX, currentY, blockSize, blue)
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        addCount(isInt,2,firstTime)
        direction=2
        moveRight(currentX, currentY, blockSize, blue)
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        addCount(isInt,3,firstTime)
        direction=3
        moveLeft(currentX, currentY, blockSize, blue)
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        addCount(isInt,4,firstTime)
        direction = 4
        moveDown(currentX, currentY, blockSize, blue)
    else:
        if checkRed() == False:#no red
            if newscreen.get_at((currentX, currentY - blockSize)) == blue:#up
                addCount(isInt,1,firstTime)
                direction = 1
                moveUp(currentX, currentY, blockSize, blue)
            elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
                addCount(isInt,2,firstTime)
                direction=2
                moveRight(currentX, currentY, blockSize, blue)
            elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
                addCount(isInt,3,firstTime)
                direction=3
                moveLeft(currentX, currentY, blockSize, blue)
            elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
                addCount(isInt,4,firstTime)
                direction = 4
                moveDown(currentX, currentY, blockSize, blue)

    
            


# ------------- OUR ALGORITHM -------------

while 0 != currentY:
#for x in range(0,10):
    getCur = newscreen.get_at((currentX, currentY))
    isInt=isIntersection()
    if direction == 1:#up
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveDown(currentX, currentY, blockSize, blue)
                moveUp(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX, currentY + blockSize)) != blue:#down
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX, currentY+blockSize, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX, currentY - blockSize)) == blue:
                moveUp(currentX, currentY, blockSize, white)
            else:
                up(white)
    elif direction == 2:#right
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveLeft(currentX, currentY, blockSize, blue)
                moveRight(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX-blockSize, currentY)) != blue:#left
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX-blockSize, currentY, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX + blockSize, currentY)) == blue:
                moveRight(currentX, currentY, blockSize, white)
            else:
                right(white)
    elif direction == 3:#left
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveRight(currentX, currentY, blockSize, blue)
                moveLeft(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX+blockSize, currentY)) != blue:#right
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX+blockSize, currentY, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersection(isInt,True)                
        else:
            if newscreen.get_at((currentX - blockSize, currentY)) == blue:
                moveLeft(currentX, currentY, blockSize, white)
            else:
                left(white)
    elif direction == 4:#down
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveUp(currentX, currentY, blockSize, blue)
                moveDown(currentX, currentY, blockSize, green)#green=used path               
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX, currentY - blockSize)) != blue:#up
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX, currentY-blockSize, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX, currentY + blockSize)) == blue:
                moveDown(currentX, currentY, blockSize, white)
            else:
                down(white)
    #-print("direction-main", direction)
    pygame.image.save(newscreen, "capture.png")
pygame.image.save(newscreen, "capture.png")

print("RIGHT PATH CHOSEN",rightCount,"TIMES")
print("LEFT PATH CHOSEN",leftCount,"TIMES")
print("FRONT PATH CHOSEN",upCount,"TIMES")
#time.sleep(5)