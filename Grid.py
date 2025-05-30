import pygame
class Grid:
    white = (200,200,200)
    black = (0,0,0)
    def __init__(self, window):
        self.gridWidth = 500
        self.gridHeight = 500
        self.squareLength = 20 #slight smaller than 22 - left space for grid lines
        self.steps = 22 #500 width and height broken into 22 steps along x and y
        self.window = window
        # self.grid = []
        
    def getGridWidth(self)->int:
        return self.gridWidth
    
    def getGridHieght(self)->int:
        return self.gridHeight

    # def createGrid(self,x,y):
    #      for i in range(0,x):
    #         self.grid.append(i)
    #         for j in range(0,y):
    #             self.grid[i][j].append(j)
    #             print(i,j)

    def drawRect(self, x:int, y:int, width = 20, height = 20, white = (200,200,200)):#width and height set to default grid height
        rect = pygame.Rect(x, y, width, height) #flipping x and y flips the grid - Rect() takes y then x 
        #see -> https://www.pygame.org/docs/ref/rect.html#pygame.Rect
        pygame.draw.rect(self.window, white, rect)
    
    def drawGrid(self, white=(200,200,200)):
        # self.drawRect()
        for col in range(0,self.gridWidth,self.steps):
            for row in range(0,self.gridHeight,self.steps):
                self.drawRect(col, row, self.squareLength, self.squareLength, self.white)
        # pygame.draw.rect(window, self.white, (10,10,10,10))