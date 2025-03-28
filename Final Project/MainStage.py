# REQUIRED PACKAGES
from SnakeBattleGame import Game
from snake import Snake

# STUDENT"S SNAKES
from MySnakeTemplate import MySnakeTemplate
from MySnakeTemplate2 import MySnakeTemplate2

# Screen dimensions
WIDTH, HEIGHT = (800, 600)
Snake.MATRIX_SIZE = (40, 30) # set the MAP size
m,n = Snake.matrix_size()    # get the MAP size
snakes = [ ]

# Main game loop
def main():
    global snakes, WIDTH, m, n
    
    # Add snakes
    snakes.append(MySnakeTemplate())
    snakes.append(MySnakeTemplate2())

    # Initialize Game() and start PyGame
    game = Game(snakes, WIDTH, m, n)
    game.start()

if __name__ == "__main__":
    main()