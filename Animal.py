import random
class Animal:

    def __init__(self,steps):
        x = random.randrange(0,500,steps) #in steps of 22 to match the drawGrid range steps
        y = random.randrange(0,500,steps)
        self.points = 1
        self.bodyCoordinates = (x,y)

    def drawAnimal(self, grid, colour=(0,0,0)):
        x,y = self.bodyCoordinates
        grid.drawRect(x,y,20,20,colour)