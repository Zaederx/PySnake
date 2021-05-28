import pygame
pygame.init()

winWidth = 1280
winHeight = 720
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("PySnake")

class Snake:
    head = 0 #collumn for head of snake
    x = 0 # key for x position of snake head
    y = 1 # key for y position of snake head 
    bodyCoordinates = [[0,0],[0,1],[0,2]] #starting body coordinates
    white = (200,200,200)
    def __init__(self):
        self.length = 1
        self.width = 10

    
    def eat(self,animal):
        self.length += 1

    def turnSnakeHead(self,direction):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_UP]: #TODO and not already moving upwards
            self.bodyCoordinates[self.head][self.y] -= 1; # move the head of the snake up
        
        if keyPressed[pygame.K_DOWN]: #TODO and not already heading downwards
            self.bodyCoordinates[self.head][self.y] += 1; #turn snake head down

        if keyPressed[pygame.K_LEFT]: #TODO and not already heading left
            self.bodyCoordinates[self.head][self.x] += 1; #turn snake head down
        
        if keyPressed[pygame.K_RIGHT]: #TODO and not already heading right
            self.bodyCoordinates[self.head][self.x] += 1; #turn snake head down

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
        
        

    def createGrid(self,x,y):
         for i in range(0,x):
            self.grid.append(i)
            for j in range(0,y):
                self.grid[i][j].append(j)
                print(i,j)

    def drawRect(self, x = 40, y = 40, width = 20, height = 20, colour = (200,200,200)):#width and height set to default grid height
        rect = pygame.Rect(y, x, width, height)
        pygame.draw.rect(window, colour, rect)
    
    def drawGrid(self, window, colour=(200,200,200)):
        # self.drawRect()
        for col in range(0,self.gridWidth,22):
            for row in range(0,self.gridHeight,22):
                self.drawRect(col, row, 20, 20, colour)
        # pygame.draw.rect(window, self.white, (10,10,10,10))
    
    def drawSnake(self, snake):
        for x,y in snake:
            self.drawRect(x*22, y*22 ,20,20, self.black)




def draw_game():
    grid = Grid()
    grid.drawGrid(window)
    snake = Snake()
    coordinates = snake.bodyCoordinates
    grid.drawSnake(coordinates)
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