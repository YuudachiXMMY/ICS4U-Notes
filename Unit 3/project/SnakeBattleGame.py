import sys
import pygame, random
from snake import Snake
from MySnakeTemplate import MySnakeTemplate

'''
Game Loop:
    1. call snakes' `move()`
    2. update snakes' `body_positions` and record the `map` information
    1. call snakes' `check_body()`
    3. draw snakes
    4. call snakes' `detect(map)`
'''
class Game:
    # Game Constants
    UPDATE_TIME = 100  # 0.1 second
    MESSAGE_TIME = 2000 # 2 second

    # GUI Constants
    GRID_COLOR = (200, 200, 200)  # Light gray
    LINE_COLOR = (200, 200, 200)  # Dark gray
    SCREEN_COLOR = (255, 255, 255)  # White
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    TITLE_SIZE = 72
    MESSAGE_SIZE = 24


    def __init__(self, snakes : list, w : int = 800, m : int = 15, n : int = 10, Caption : str = 'Battle Grid'):
        """Initialize Game object."""
        # Initialize pygame
        pygame.init()

        self.map : list[list[list]] = [[[] for _ in range(m)] for _ in range(n)]

        # Player Initializing
        self.snakes : list[Snake] = snakes

        # Screen dimensions
        self.m : int = m
        self.n : int = n
        self.WIDTH : int = w
        self.cell_size : int = w // m
        self.HEIGHT : int = n * self.cell_size

        self.screen : pygame.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.caption = pygame.display.set_caption(Caption)
        self.title : pygame.font.Font = pygame.font.SysFont(None, Game.TITLE_SIZE)
        self.message : pygame.font.Font = pygame.font.SysFont(None, Game.MESSAGE_SIZE)

        self.deads : list[str] = []
        self.winners : list[Snake] = []

        self.last_message_time = pygame.time.get_ticks()
        self.last_update_time = pygame.time.get_ticks()
        self.clock = None
        self.running : bool = False

    def check_end(self) -> bool:
        if len(self.snakes) == 1:
            self.winners.append(self.snakes[0])
            return True
        return False

    def move(self):
        i = 0
        while i < len(self.snakes):
            status = self.snakes[i].move()
            if not status:
                # print(f'{self.snakes[i].name} is disqualified or dead!')
                # self.draw_deads(self.snakes[i].name)
                self.deads.append(self.snakes[i].name)
                self.snakes.pop(i)
            i += 1

        self.draw_deads()
        self.update_data()

        for snake in self.snakes:
            snake.check_body()

        for snake in self.snakes:
            self.draw_snake(snake)

        for snake in self.snakes:
            snake.detect(self.map)

    def update_data(self):
        for i in range(len(self.snakes)):
            x, y, hp = self.snakes[i].body_positions[0]
            if not ((0 <= x and x < self.m) and (0 <= y and x < self.n)):
                continue
            for j in range(len(self.snakes)):
                if i == j:
                    continue
                for k in range(len(self.snakes[j].body_positions)):
                    bx,by,bhp = self.snakes[j].body_positions[k]
                    if bx == x and by == y:
                        self.snakes[j].body_positions[k] = (bx, by, bhp-self.snakes[i].attack)
                        break
            self.map[x][y].append(hp)

    def start(self):
        """Start the game loop."""
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            end = self.check_end()
            if not end:
                self.update()
            else:
                self.draw_ending()


            pygame.display.flip()
            self.clock.tick(30)  # Limit to 30 frames per second

        self.exit()

        self.update()

    def update(self):
        """Main game loop."""
        if self._checkTime(self.last_update_time):
            self.draw_grid()

            self.move()

            self.last_update_time = pygame.time.get_ticks()

    def exit(self):
        """Exit game."""
        pygame.quit()
        sys.exit()

    def _checkTime(self, last : int) -> bool:
        current_time = pygame.time.get_ticks()
        return current_time - last > Game.UPDATE_TIME

    # Main loop
    def draw_snake(self, snake : Snake):
        deep = 0.5
        color = snake.color
        for i in range(len(snake.body_positions)-1, -1, -1):
            body = snake.body_positions[i]
            if i == 0:
                color = tuple(c * deep for c in color)
            x, y, hp = body
            if hp < 1:
                break
            pygame.draw.rect(self.screen, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def draw_grid(self):
        """Draw the grid on the screen."""
        self.screen.fill(Game.SCREEN_COLOR)
        for row in range(self.n + 1):
            pygame.draw.line(self.screen, Game.LINE_COLOR, (0, row * self.cell_size), (self.WIDTH, row * self.cell_size))
        for col in range(self.m + 1):
            pygame.draw.line(self.screen, Game.LINE_COLOR, (col * self.cell_size, 0), (col * self.cell_size, self.HEIGHT))

    def draw_deads(self):
        """Show Ending Message"""
        if self._checkTime(self.last_message_time):
            for i in range(len(self.deads)):
                self._draw_deads(self.deads[i], i)
            self.last_message_time = pygame.time.get_ticks()

    def _draw_deads(self, name, i):
        txt = '{name} is disqualified or dead!'.format(name=name)
        text = self.message.render(txt, True, Game.RED)
        self.screen.blit(text, (Game.MESSAGE_SIZE / 2, Game.MESSAGE_SIZE / 2+Game.MESSAGE_SIZE*i))

    def draw_ending(self):
        """Show Ending Message"""
        txt = "{snake} win!".format(snake=self.snakes[0].name)
        text = self.title.render(txt, True, Game.RED)
        text_rect = text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.screen.blit(text, text_rect)