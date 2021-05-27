import pygame
pygame.init()

winWidth = 1280
winHeight = 720
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("PySnake")

class Snake:
    bodyCoordinates = [0,0]
    def __init__(self):
        self.length = 1
        self.width = 10

    
    def eat(self,animal):
        self.length += 1

    def drawSnake():
        pygame.draw.rect

class Animal:
    def __init__(self):
        self.points
        

class Grid:
    
    def __init__(self, x, y):
        self.grid = []
        self.createGrid(x,y)
        
    def createGrid(self,x,y):
         for i in range(0,x):
            self.grid.append(i)
            for j in range(0,y):
                self.grid[i][j].append(j)
                print(i,j)