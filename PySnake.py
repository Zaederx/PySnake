import pygame
import Snake
import Animal
from pygame import display
pygame.init()
steps = 22
winWidth = 1280
winHeight = 720
window = pygame.display.set_mode((winWidth, winHeight))
window.fill((0,0,0))
pygame.display.set_caption("PySnake")




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
        for col in range(0,self.gridWidth,steps):
            for row in range(0,self.gridHeight,steps):
                self.drawRect(col, row, 20, 20, colour)
        # pygame.draw.rect(window, self.white, (10,10,10,10))
    
grid = Grid()
# grid.drawGrid(window)
snake = Snake.Snake() #must remain outside of game loop - otherwise direction is always reset to right
animal = Animal.Animal(steps)

def draw_game():
    window.fill((0,0,0))
    grid = Grid()
    grid.drawGrid(window)
    snake.drawSnake(grid,steps)
    snake.move(grid)
    snake.turnSnakeHead()
    snake.displayScore(window)
    animal.drawAnimal(grid)
    pygame.display.flip()
    pygame.display.update()

run = True
while run: 
    pygame.time.delay(90)
    draw_game()
    # print("Just Checking")
    x,y = animal.bodyCoordinates
    # print("x:",x,"y:",y)
    sx,sy = snake.getSnakeHead()
    # print("sx:",sx,"sy:",sy)
    if x == sx*steps and  y == sy*steps :
        snake.eat(animal)
        print("Snake length:"+str(snake.length)
        )
        print("NEW ANIMAL")
        animal = Animal.Animal(steps)
        animal.drawAnimal(grid)
        pygame.display.flip()

    # pygame.draw.rect(window, (), (10,10,10,10))      
    

    # Quiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False