from typing import final, Optional, Final
import random
from dataclasses import dataclass

@dataclass(frozen=True)
class SnakeConfig:
    SEED: Final[int] = 31415926535897932384
    ATTRIBUTE_RESTRICTION: Final[int] = 200
    MATRIX_SIZE: Final[tuple[int, int]] = (40, 30)

class Snake:

    @staticmethod
    def matrix_size() -> tuple[int, int]:
        """
        Return the map size as a tuple (m, n).
        """
        return SnakeConfig.MATRIX_SIZE

    def __init__(self, start_x: int, start_y: int, color: tuple[int, int, int],
                 name: str, length: int, attack: int, hp: int) -> None:
        """
        Initialize the Snake object.

        Args:
            start_x: Starting x-coordinate in grid units (0 to MATRIX_SIZE[0]-1)
            start_y: Starting y-coordinate in grid units (0 to MATRIX_SIZE[1]-1)
            color: RGB color tuple with values between 0-255
            name: The name of the snake
            length: Initial length of the snake
            attack: Attack power of the snake
            hp: Initial health points of the snake

        Raises:
            ValueError: If color values are invalid or position is out of bounds

        :param start_x: Starting x-coordinate in grid units.
        :param start_y: Starting y-coordinate in grid units.
        :param length: Initial Length of the snake.
        :param color: The color of the snake (can be used for visualization later).
        :param name: The name of the snake (can be used for visualization later).
        """
        random.seed(SnakeConfig.SEED)
        self._validate_color(color)
        self._validate_position(start_x, start_y)

        self.body_positions: list[tuple[int, int, int]] = []
        if length + attack + hp > SnakeConfig.ATTRIBUTE_RESTRICTION:
            self.length: int = 0
        else:
            self.body_positions = [(start_x, start_y, hp)]
            self.length: int = length
        self.color: tuple[int, int, int] = color
        self.name: str = name
        self.attack: int = attack
        self.hp: int = hp

    @staticmethod
    def _validate_color(color: tuple[int, int, int]) -> None:
        if not all(0 <= c <= 255 for c in color):
            raise ValueError("Color values must be between 0 and 255")

    @staticmethod
    def _validate_position(x: int, y: int) -> None:
        if not (0 <= x < SnakeConfig.MATRIX_SIZE[0] and 0 <= y < SnakeConfig.MATRIX_SIZE[1]):
            raise ValueError("Position out of bounds")

    # You can feel free to override this method.
    def detect(self, game_map: list[list[list[int]]]) -> None:
        """
        Process the game map to make movement decisions.
        TODO: You could implement your own Detect for your move()

        Args:
            game_map: 3D list representing the game state where:
                     - First dimension is x coordinate
                     - Second dimension is y coordinate
                     - Third dimension contains game object information

        Returns:
            None
        """
        pass

    @property# We'll fire you if you override this method.
    def qualification(self) -> bool:
        """
        Check if the snake is qualified to play the game.

        :return: True if the snake is qualified, False otherwise.
        """
        return self.length > 0

    @final # We'll fire you if you override this method.
    def move(self, direction: tuple[int, int]) -> Optional[tuple[int, int]]:
        """
        Move the snake in the specified direction.

        Args:
            direction: Tuple (dx, dy) indicating movement direction:
                     (1,0) right, (-1,0) left, (0,1) down, (0,-1) up

        Returns:
            The direction moved if successful, None if the snake is dead or disqualified

        :param direction: Tuple (dx, dy) indicating the direction (e.g., (1, 0) for right).
        :return: True if the move is successful, False otherwise.
        """
        if not self.qualification or self.isDead():
            return None

        head_x, head_y, hp = self.body_positions[0]
        new_head = (head_x + direction[0], head_y + direction[1], hp)

        if self.check_collision():
            self.length -= 1
            del self.body_positions[0]

        if not self.qualification or self.isDead():
            return None

        # Insert the new head and remove the last segment if the length remains the same
        self.body_positions = [new_head] + self.body_positions[:self.length - 1]

        return direction

    @final# We'll fire you if you override this method.
    def grow(self) -> None:
        """
        Increase the length of the snake by 1.

        ONLY call this method when you are testing your snake in the main()
        """
        self.length += 1
        # No need to modify body_positions as the tail will naturally grow with subsequent moves

    @final# We'll fire you if you override this method.
    def isDead(self) -> bool:
        """
        Check if the snake is dead.
        """
        return self.length < 1 or self.body_positions[0][2] < 1

    @final# We'll fire you if you override this method.
    def check_collision(self) -> bool:
        """
        Check for collisions with the boundaries or itself.

        DO NOT USE this method to write your _checkCollision()!!! The requirements are different.

        :return: True if a collision is detected, False otherwise.
        """
        if self.length < 1:
            return False
        bodies = [[x,y] for x,y,hp in self.body_positions]
        head = bodies[0]
        # Check for boundary collision
        if not (0 <= head[0] < SnakeConfig.MATRIX_SIZE[0] and 0 <= head[1] < SnakeConfig.MATRIX_SIZE[1]):
            return True
        # Check for self-collision
        if self.length > 1 and head in bodies[1:]:
            return True
        return False

    @final# We'll fire you if you override this method.
    def check_body(self) -> None:
        """
        Check if the body is still alive and remove the dead segments.
        """
        for i in range(1, len(self.body_positions)):
            x, y, hp = self.body_positions[i]
            if hp < 1:
                self.body_positions = self.body_positions[:i]
                self.length = i
                break
        if len(self.body_positions) < 1:
            self.length = 0

    @final# We'll fire you if you override this method.
    def __str__(self):
        """
        ToString() of the snake.
        """
        return self.__repr__()

    @final# We'll fire you if you override this method.
    def __repr__(self):
        """
        String representation of the snake for debugging.
        """
        return f"Snake({self.name}, {self.color}, {self.hp}, {self.attack}, {self.length}, {self.body_positions})"
