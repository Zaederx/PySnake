import pygame
pygame.init()

winWidth = 1280
winHeight = 720
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("PySnake")

class Snake:
    up = 1
    down = 2
    left = 3
    right = 4
    black=(0,0,0)
    head = 0 #collumn for head of snake
    x = 0 # key for x position of snake head
    y = 1 # key for y position of snake head 
    bodyCoordinates = [[0,0],[0,1],[0,2]] #starting body coordinates
    white = (200,200,200)
    def __init__(self):
        self.length = 1
        self.width = 10
        self.direction = self.right

    
    def eat(self,animal):
        self.length += 1
    
    def drawSnake(self,grid):
        for x,y in self.bodyCoordinates:
            grid.drawRect(x*22, y*22 ,20,20, self.black)
    
    #changes 'head' coordinate trajectory
    def turnSnakeHead(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_UP]: #TODO and not already moving upwards
            self.bodyCoordinates[self.head][self.y] -= 1; # move the head of the snake up
        
        if keyPressed[pygame.K_DOWN]: #TODO and not already heading downwards
            self.bodyCoordinates[self.head][self.y] += 1; #turn snake head down

        if keyPressed[pygame.K_LEFT]: #TODO and not already heading left
            self.bodyCoordinates[self.head][self.x] += 1; #turn snake head down
        
        if keyPressed[pygame.K_RIGHT]: #TODO and not already heading right
            self.bodyCoordinates[self.head][self.x] += 1; #turn snake head down
    
    def getSnakeHead(self):
        x = self.bodyCoordinates[self.head][self.x]
        y = self.bodyCoordinates[self.head][self.y]
        return (x,y)
    
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

        if self.direction == self.left:
            x -= 1
        
        if self.direction == self.up:
            y -= 1

        if self.direction == self.down:
            y += 1

        #insert head
        self.bodyCoordinates.insert(0,[x,y])
    
    #pop tail
    def popTail(self):
        self.bodyCoordinates.pop()

    #moves the snake a block forward in the current trajectory
    def move(self):
        self.placeHead()
        self.popTail()
        
        

class Animal:
    def __init__(self):
        self.points
        

class Grid:
    white = (200,200,200)
    black = (0,0,0)
    def __init__(self):
        self.gridWidth = 500
        self.gridHeight = 500
        # self.grid = []
        

    # def createGrid(self,x,y):
    #      for i in range(0,x):
    #         self.grid.append(i)
    #         for j in range(0,y):
    #             self.grid[i][j].append(j)
    #             print(i,j)

    def drawRect(self, x = 40, y = 40, width = 20, height = 20, colour = (200,200,200)):#width and height set to default grid height
        rect = pygame.Rect(x, y, width, height) #flipping x and y flips the grid - Rect() takes y then x 
        #see -> https://www.pygame.org/docs/ref/rect.html#pygame.Rect
        pygame.draw.rect(window, colour, rect)
    
    def drawGrid(self, window, colour=(200,200,200)):
        # self.drawRect()
        for col in range(0,self.gridWidth,22):
            for row in range(0,self.gridHeight,22):
                self.drawRect(col, row, 20, 20, colour)
        # pygame.draw.rect(window, self.white, (10,10,10,10))
    



def draw_game():
    grid = Grid()
    grid.drawGrid(window)
    snake = Snake()
    
    snake.drawSnake(grid)
    snake.move()
    pygame.display.flip()
    # pygame.display.update()

run = True
while run: 
    pygame.time.delay(50)
    draw_game()
    # pygame.draw.rect(window, (), (10,10,10,10))      
    

    # Quiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False