import pygame
import Grid
class Snake:
    up = 1
    down = 2
    left = 3
    right = 4
    black=(0,0,0)
    head = 0 #collumn for head of snake
    x = 0 # key for x position of snake head
    y = 1 # key for y position of snake head 
    bodyCoordinates = [[2,0],[3,0],[4,0]] #starting body coordinates
    white = (200,200,200)
    def __init__(self):
        self.length = 1
        self.direction = self.right

    
    def eat(self,animal):
        print("Snake eats animal")
        self.length += animal.points
        self.bodyCoordinates.append([-1,-1])
    
    def drawSnake(self,grid:Grid,steps):
        for x,y in self.bodyCoordinates:
            # x and y are values between 1 and 22 (grid is 500px in 22 blocks)
            # steps / division by 22 also means that the distance or length of each square is also 22(.7)
            #so you can approximate and use 22 as the multiplier for the coordinate
            grid.drawRect(x*grid.steps, y*grid.steps, 20, 20, self.black) #in steps of 22 pixels to allow the gaps
    
    #changes 'head' coordinate trajectory
    def turnSnakeHead(self):
        x = self.bodyCoordinates[self.head][self.x]
        y = self.bodyCoordinates[self.head][self.y]
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_UP]: #TODO and not already moving upwards
            y -= 1; # move the head of the snake up
            self.direction = self.up #TODO uncomment to turn off free roam mode

        if keyPressed[pygame.K_DOWN]: #TODO and not already heading downwards
            y += 1; #turn snake head down
            self.direction = self.down #TODO uncomment to turn off free roam mode

        if keyPressed[pygame.K_LEFT]: #TODO and not already heading left
            x -= 1; #turn snake head down
            self.direction = self.left #TODO uncomment to turn off free roam mode
        
        if keyPressed[pygame.K_RIGHT]: #TODO and not already heading right
            x += 1; #turn snake head down
            self.direction = self.right #TODO uncomment to turn off free roam mode
        
        # update bodyCoordinates with changes
        self.bodyCoordinates[self.head][self.x] = x
        self.bodyCoordinates[self.head][self.y] = y


    def getSnakeHead(self):
        x = self.bodyCoordinates[self.head][self.x]
        y = self.bodyCoordinates[self.head][self.y]
        return x,y
    
    def getDirection(self):
        return self.direction

    def setSnakeHead(self, x, y):
        self.bodyCoordinates[self.head][self.x] = x
        self.bodyCoordinates[self.head][self.y] = y

    #places new head block at the new coordinates
    #assumes coordinates for head have been already changed
    def placeHead(self):
        #get head coordinates
        x,y = self.getSnakeHead()

        #get head direction
        if self.direction == self.right:
            x += 1
            if x >= 23:
                x = -1

        if self.direction == self.left:
            x -= 1
            if x <= -1:
                x = 23
        if self.direction == self.up:
            y -= 1
            if y <= -1:
                y = 23

        if self.direction == self.down:
            y += 1
            if y >= 23:
                y = -1
        
                #stop snake movement
        #insert head
        self.bodyCoordinates.insert(0,[x,y])
    
    #pop tail
    def popTail(self):
        # x,y = self.bodyCoordinates[-1]
        # grid.drawRect(x,y,20,20,self.white)
        self.bodyCoordinates.pop()

    #moves the snake a block forward in the current trajectory
    def move(self):
        self.placeHead()
        self.popTail()
        
    def displayScore(self, window):
        font = pygame.font.Font(None, 100)
        text = font.render("Score:" + str(self.length), True, self.white)
        textX = 800
        textY = 50
        window.blit(text,(textX,textY))
        