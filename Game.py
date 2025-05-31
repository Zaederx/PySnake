import pygame
import Grid
import Snake
import Animal

# Note: pygame.display.update() - updates a portion of the screen that it needs to
# pygame.display.flip() - updates the entire screen
class Game:
    def __init__(self, window):
        pygame.init()
        self.winWidth = 1280
        self.winHeight = 720
        self.window = window
        self.window.fill((0,0,0))
        pygame.display.set_caption("PySnake")
        self.black=(0,0,0)
        self.white = (200,200,200) 
        self.grid = Grid.Grid(self.window)
        # grid.drawGrid(window)
        self.snake = Snake.Snake() #must remain outside of game loop - otherwise direction is always reset to right
        self.animal = Animal.Animal(self.grid.steps)
        self.loop = 0
        self.run = True

    def isGameOver(self):
        #check if snake head meets snake body
        sx,sy = self.snake.getSnakeHead();
        # print("coordinate length",len(self.snake.bodyCoordinates))
        for i in range(1,len(self.snake.bodyCoordinates)):
            if self.snake.bodyCoordinates[i] == [sx,sy]:
                # print("i",i)
                # print("snake body:", self.snake.bodyCoordinates[i], "sx,sy:",[sx,sy])
                return True
            else:
                return False

    def endGame(self):
        # draw_game()
        self.displayEndMessage()
        self.run = False
        

    def displayEndMessage(self):
        # prepare text
        font1 = pygame.font.Font(None, 100)
        font2 = pygame.font.Font(None, 35)
        text1 = font1.render("Game Over! Score:" + str(self.snake.length),True,self.white)
        text2 = font2.render('Press "Spacebar" on the keyboard to restart/play again', True, self.white)
        #text position values
        text1X = 550
        text1Y = 50
        text2X = 550
        text2Y = 150
        # display text
        self.window.blit(text1,(text1X,text1Y))
        self.window.blit(text2,(text2X,text2Y))
        

    # check if animal should be move (happens after being eaten by snake)
    def reassignAnimalBool(self):
        # print("Just Checking")
        x,y = self.animal.bodyCoordinates
        # print("x:",x,"y:",y)
        sx,sy = self.snake.getSnakeHead()
        # print("sx:",sx,"sy:",sy)
        # snake-x (sx) * steps because that equates to how many squares you move across (on a 500px/22px = 22.7 GRID, so I'll just approxitamte and use the steps variables which is 22)
        if x == sx*self.grid.steps and  y == sy*self.grid.steps : 
            return True

    # reassign the animal
    def reassignAnimal(self):
        self.animal = Animal.Animal(self.grid.steps)
        self.animal.drawAnimal(self.grid)
        pygame.display.flip()
        return self.animal


    def draw_game(self):
        self.grid.drawGrid(self.grid)
        self.snake.turnSnakeHead()
        self.snake.drawSnake(self.grid)
        self.animal.drawAnimal(self.grid)
        self.snake.displayScore(self.window)
        pygame.display.update()

        # pygame.draw.rect(window, (), (10,10,10,10))   
    def draw_game_end(self):
        self.grid.drawGrid(self.grid.steps)
        self.snake.drawSnake(self.grid)
        self.animal.drawAnimal(self.grid)
        self.displayEndMessage()
        pygame.display.update()

        
    def resetGame(self):
        self.snake = Snake.Snake()
        self.loop = 0
    def playGame(self):
        # Note: for some reason exiting the game loop
        # exists the window
        while self.run:
            self.window.fill((0,0,0))
            # print("loop:",self.loop)
            pygame.time.delay(90)
            
            if self.loop == 0 or self.isGameOver() == False:
                self.loop += 1
                self.snake.move()#game doesn't end on collision if not in this order
                self.draw_game()
            else:
                self.draw_game_end()

            #reassign Animal if eaten
            if self.reassignAnimalBool():
                self.snake.eat(self.animal)
                print("Snake length:"+str(self.snake.length))
                print("NEW ANIMAL")
                self.animal = self.reassignAnimal()
                pygame.display.update()

            # Quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.K_SPACE:#doesn't get triggered for some reason
                    print('Spacebar pressed')
                    self.resetGame()

            # pygame.display.flip()
            # pygame.display.update()