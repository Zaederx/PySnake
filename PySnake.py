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





    
grid = Grid.Grid(window)
# grid.drawGrid(window)
snake = Snake.Snake() #must remain outside of game loop - otherwise direction is always reset to right
animal = Animal.Animal(steps)

def draw_game():
    window.fill((0,0,0))
    grid.drawGrid(steps)
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
    print("sx:",sx,"sy:",sy)
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