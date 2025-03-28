from typing import final
import random

class Snake:

    SEED : int = 31415926535897932384
    ATTRIBUTE_RESTRICTION : int = 200
    MATRIX_SIZE : tuple[int, int] = (40, 30)

    @staticmethod
    def matrix_size() -> tuple[int, int]:
        """
        Return the map size as a tuple (m, n).
        """
        return Snake.MATRIX_SIZE

    def __init__(self, start_x : int, start_y : int, color : tuple[int, int, int],
                 name : str, length : int, attack : int, hp : int):
        """
        Initialize the Snake object.

        :param start_x: Starting x-coordinate in grid units.
        :param start_y: Starting y-coordinate in grid units.
        :param length: Initial Length of the snake.
        :param color: The color of the snake (can be used for visualization later).
        :param name: The name of the snake (can be used for visualization later).
        """
        random.seed(Snake.SEED)

        self.body_positions : list[tuple[int, int, int]] = []
        if length + attack + hp > Snake.ATTRIBUTE_RESTRICTION:
            self.length : int = 0
        else:
            self.body_positions = [(start_x, start_y, hp)]
            self.length : int = length
        self.color : tuple[int, int, int] = color
        self.name : str = name
        self.attack : int = attack
        self.hp : int = hp

    # You can feel free to override this method.
    def detect(self, map : list[list[list[int]]]) -> None:
        """
        Do nothing. Feel Free to override!

        TODO: You could implement your own Detect for your move()
        """
        pass

    @property # We'll fire you if you override this method.
    def qualification(self) -> bool:
        """
        Check if the snake is qualified to play the game.

        :return: True if the snake is qualified, False otherwise.
        """
        return self.length > 0

    @final # We'll fire you if you override this method.
    def move(self, direction : list[int, int]) -> list:
        """
        Move the snake in a specified direction. return False if the snake is disqualified or dead.

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

    @final # We'll fire you if you override this method.
    def grow(self) -> None:
        """
        Increase the length of the snake by 1.

        ONLY call this method when you are testing your snake in the main()
        """
        self.length += 1
        # No need to modify body_positions as the tail will naturally grow with subsequent moves

    @final # We'll fire you if you override this method.
    def isDead(self) -> bool:
        """
        Check if the snake is dead.
        """
        return self.length < 1 or self.body_positions[0][2] < 1

    @final # We'll fire you if you override this method.
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
        if not (0 <= head[0] < Snake.MATRIX_SIZE[0] and 0 <= head[1] < Snake.MATRIX_SIZE[1]):
            return True
        # Check for self-collision
        if self.length > 1 and head in bodies[1:]:
            return True
        return False

    @final # We'll fire you if you override this method.
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

    @final # We'll fire you if you override this method.
    def __str__(self):
        """
        ToString() of the snake.
        """
        return self.__repr__()

    @final # We'll fire you if you override this method.
    def __repr__(self):
        """
        String representation of the snake for debugging.
        """
        return f"Snake({self.name}, {self.color}, {self.hp}, {self.attack}, {self.length}, {self.body_positions})"
