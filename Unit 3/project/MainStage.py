import pygame
import random
import sys
from SnakeBattleGame import Game
from snake import Snake

from MySnakeTemplate import MySnakeTemplate
from MySnakeTemplate2 import MySnakeTemplate2
from MySnakeTemplate3 import MySnakeTemplate3

# Screen dimensions
WIDTH, HEIGHT = 800, 600


# Main game loop
def main():
    m,n = Snake.matrix_size()
    snakes = [ ]
    snakes.append(MySnakeTemplate())
    snakes.append(MySnakeTemplate2())
    snakes.append(MySnakeTemplate3())

    game = Game(snakes, 800, m, n)
    game.start()

if __name__ == "__main__":
    main()