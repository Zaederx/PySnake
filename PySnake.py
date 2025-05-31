import Game
import pygame
width = 1280
height = 720
window = pygame.display.set_mode((width, height))
game = Game.Game(window)
game.playGame()