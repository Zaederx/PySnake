import pygame
import Grid
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
black=(0,0,0)
white = (200,200,200) 
grid = Grid.Grid(window)
# grid.drawGrid(window)
snake = Snake.Snake() #must remain outside of game loop - otherwise direction is always reset to right
animal = Animal.Animal(steps)

def isGameOver():
    #if snake head meets snake body
    sx,sy = snake.getSnakeHead();
    for i in range(1,len(snake.bodyCoordinates)):
        if snake.bodyCoordinates[i] == [sx,sy]:
            return True
        else:
            return False

def endGame(snake):
    # draw_game()
    displayEndTitle(snake)
    pygame.display.update()

def displayEndTitle(snake):
    font = pygame.font.Font(None, 100)
    text = font.render("Game Over! Score:" + str(snake.length), True, white)
    textX = 800
    textY = 50
    window.blit(text,(textX,textY))
    pygame.display.update()

# check if animal should be move (happens after being eaten by snake)
def reassignAnimalBool(animal):
     # print("Just Checking")
    x,y = animal.bodyCoordinates
    # print("x:",x,"y:",y)
    sx,sy = snake.getSnakeHead()
    print("sx:",sx,"sy:",sy)
    if x == sx*steps and  y == sy*steps :
        return True

# reassign the animal
def reassignAnimal(animal):
    animal = Animal.Animal(steps)
    animal.drawAnimal(grid)
    pygame.display.flip()
    return animal

def draw_game():
    window.fill((0,0,0))
    grid.drawGrid(steps)
    snake.drawSnake(grid,steps)
    snake.turnSnakeHead()
    animal.drawAnimal(grid)
    
    

    if isGameOver() == False:
        snake.move(grid)
    else:
        snake.displayScore(window)
        endGame(snake)
    # pygame.draw.rect(window, (), (10,10,10,10))      
    

    

run = True
while run: 
    pygame.time.delay(90)
    draw_game()
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



pygame.display.flip()
pygame.display.update()