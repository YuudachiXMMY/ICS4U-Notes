import sys
import pygame
import random

# Basic Variables
COLORS = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (128, 0, 128)  # Purple
]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Shape:
    def __init__(self, shape_type, x, y, color):
        self.shape_type = shape_type  # 'circle' or 'rectangle'
        self.x = x
        self.y = y
        self.color = color

class Rectangle(Shape):
    def __init__(self, shape_type, x, y, width, height, color):
        super().__init__(shape_type, x, y, color) # Inherit from the Shape class
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def is_clicked(self, pos):
        return (self.x <= pos[0] and pos[0] <= self.x + self.width) and \
               (self.y <= pos[1] and pos[1] <= self.y + self.height)


class Circle(Shape):
    def __init__(self, shape_type, x, y, radius, color):
        super().__init__(shape_type, x, y, color) # Inherit from the Shape class
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        distance = ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) ** 0.5
        return distance <= self.radius

class Game:
    SHAPE_LIFETIME = 3000
    NUM_SHAPES = 10

    def __init__(self, width=800, height=600, caption="New Game", font_size=36):
        pygame.init()
        self.windowWidth = width
        self.windowHeight = height
        self.screen = pygame.display.set_mode((width, height))
        self.caption = pygame.display.set_caption(caption)
        self.font = pygame.font.SysFont(None, font_size)
        self.clock = pygame.time.Clock()

        self.score = 0
        self.shapes = []
        self.target_color = random.choice(COLORS)

        self.last_spawn_time = pygame.time.get_ticks()

    def start(self):
        self.running = True
        self.spawn_shapes()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def stop(self):
        self.running = False

    def update(self):
        # Check if it's time to spawn new shapes
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > self.SHAPE_LIFETIME:
            self.spawn_shapes()
            self.last_spawn_time = current_time

    def spawn_shapes(self):
        # TODO: Generate a list of shapes.
        # Each Shape should have a random shape_type, x, y, width, height, and color.
        self.shapes = []
        for _ in range(self.NUM_SHAPES):
            shape_type = random.choice(['circle', 'rectangle'])
            width = random.randint(30, 100)
            height = width if shape_type == 'circle' else random.randint(30, 100)
            x = random.randint(0, self.windowWidth - width)
            y = random.randint(35+height, self.windowHeight - height)
            color = random.choice(COLORS)
            if shape_type == 'circle':
                self.shapes.append(Circle(shape_type, x, y, width//2, color))
            else:
                self.shapes.append(Rectangle(shape_type, x, y, width, height, color))

    def draw(self):
        # Fill the background with WHITE color
        self.screen.fill(WHITE)

        # Draw the Shapes using the list of shapes.
        for shape in self.shapes:
            shape.draw(self.screen)

        # Draw target color
        pygame.draw.rect(self.screen, self.target_color, (0, 0, 800, 35))

        # Draw scoreboard
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (300, 10))


    def handle_click(self, pos):
        for shape in self.shapes[:]:
            if shape.is_clicked(pos):
                if shape.color == self.target_color:
                    self.score += 1
                else:
                    self.score = 0
                self.shapes.remove(shape)
                break