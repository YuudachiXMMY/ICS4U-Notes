import pygame
import random
import sys
from PyGame_ColorClicking import Game

# Screen dimensions
WIDTH, HEIGHT = 800, 600


# Main game loop
def main():
    game = Game(WIDTH, HEIGHT, "Color Click Game")
    game.start()

if __name__ == "__main__":
    main()