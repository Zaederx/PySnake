import pygame
class Grid:
    white = (200,200,200)
    black = (0,0,0)
    def __init__(self, window):
        self.gridWidth = 500
        self.gridHeight = 500
        self.window = window
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
        pygame.draw.rect(self.window, colour, rect)
    
    def drawGrid(self, steps, colour=(200,200,200)):
        # self.drawRect()
        for col in range(0,self.gridWidth,steps):
            for row in range(0,self.gridHeight,steps):
                self.drawRect(col, row, 20, 20, colour)
        # pygame.draw.rect(window, self.white, (10,10,10,10))