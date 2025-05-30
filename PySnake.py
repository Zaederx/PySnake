import pygame
import Grid
import Snake
import Animal
pygame.init()


winWidth = 1280
winHeight = 720
window = pygame.display.set_mode((winWidth, winHeight))
window.fill((0,0,0))
pygame.display.set_caption("PySnake")
black=(0,0,0)
white = (200,200,200) 
grid = Grid.Grid(window)
# grid.drawGrid(window)
snake = Snake.Snake() #must remain outside of game loop - otherwise direction is always reset to right
animal = Animal.Animal(grid.steps)

def isGameOver():
    #if snake head meets snake body
    sx,sy = snake.getSnakeHead();
    print("coordinate length",len(snake.bodyCoordinates))
    for i in range(1,len(snake.bodyCoordinates)):
        if snake.bodyCoordinates[i] == [sx,sy]:
            print("i",i)
            print("snake body:",snake.bodyCoordinates[i], "sx,sy:",[sx,sy])
            return True
        else:
            return False

def endGame(snake):
    # draw_game()
    displayEndTitle(snake)

def displayEndTitle(snake):
    font = pygame.font.Font(None, 100)
    text = font.render("Game Over! Score:" + str(snake.length), True, white)
    textX = 550
    textY = 50
    window.blit(text,(textX,textY))
    

# check if animal should be move (happens after being eaten by snake)
def reassignAnimalBool(animal):
     # print("Just Checking")
    x,y = animal.bodyCoordinates
    # print("x:",x,"y:",y)
    sx,sy = snake.getSnakeHead()
    print("sx:",sx,"sy:",sy)
    # snake-x (sx) * steps because that equates to how many squares you move across (on a 500px/22px = 22.7 GRID, so I'll just approxitamte and use the steps variables which is 22)
    if x == sx*grid.steps and  y == sy*grid.steps : 
        return True

# reassign the animal
def reassignAnimal(animal):
    animal = Animal.Animal(grid.steps)
    animal.drawAnimal(grid)
    pygame.display.flip()
    return animal


def draw_game():
    grid.drawGrid(grid.steps)
    snake.turnSnakeHead()
    snake.drawSnake(grid,grid.steps)
    animal.drawAnimal(grid)
    snake.displayScore(window)
    pygame.display.update()
    
    # pygame.draw.rect(window, (), (10,10,10,10))      

    
loop = 0
run = True
while run:
    window.fill((0,0,0))
    print("loop:",loop)
    pygame.time.delay(90)
    

    if loop == 0 or isGameOver() == False:
        loop += 1
        snake.move()#game doesn't end on collision if not in this order
        
        draw_game()
        
        
    else:
        grid.drawGrid(grid.steps)
        snake.drawSnake(grid,grid.steps)
        animal.drawAnimal(grid)
        endGame(snake)
        pygame.display.update()
    #reassign Animal if eaten
    if reassignAnimalBool(animal):
        snake.eat(animal)
        print("Snake length:"+str(snake.length))
        print("NEW ANIMAL")
        animal = reassignAnimal(animal)
    
    
    pygame.display.update()
    # Quiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



# pygame.display.flip()
# pygame.display.update()