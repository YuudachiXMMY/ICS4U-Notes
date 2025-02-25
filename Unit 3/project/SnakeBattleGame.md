# Snake Battle Game

You will use the given code `snake.py` to inherit your own snake and battle with other snakes.

## Getting Started

1. Download the `snake.py` and place under your working directory.
2. You can either inherit the snake by yourself, or use the `MySnakeTemplae.py`. To use the template:

   1. Change the file name `MySnakeTemplate.py` to your own/nick name
   2. Change the class name `MySnakeTemplate` to your own/nick name
   3. Implement the TODO sections

## Rules

1. Your snake attributes `length`, `attack`, and `hp` should be added up to a MAXIMUM of `200`; otherwise it will be considered `disqualified` and will be REMOVE from the game.
2. If your snake has any errors during the `detect()` and `move()`, it will have a high possibility to be removed from the game!
3. Game Loops:
    1. call snakes' `detect(map)`
    2. call snakes' `move()`
    3. update snakes' `body_positions` and record the `map` information
    4. call snakes' `check_body()`
    5. draw snakes
4. If you are using `random`, please notice that the random seed is setted to `31415926535897932384` for all snakes.

## Attributes

- `:ATTRIBUTE_RESTRICTION: int` : maximum value of the sum of `length`, `attack`, and `hp`.

- `:MATRIX_SIZE: tuple[int, int]` : map/matrix size

- `:color: tuple[int, int, int]`** : color of your snake

- `:name: str`** : name of your snake

- `:attack: int`** : attack of your snake

- `:hp: int`** : health point of your snake

- `:length: int`** : initial/total length of your snake

- `:body_positions: tuple[int, int, int]` : body positions of your snake

**NOTICE:** attributes with ** should be initialized while constructing the snake.

## Function Specification

**NOTICE:** functions with ** MUST be implemented.

### `move()`**

Return the direction to move the snake.

`::return::` : `list[int]` : the direction of the next move. Value should be one of the following:

- `[-1, 0]`
- `[1, 0]`
- `[0, -1]`
- `[0, 1]`

**HINT:** Avoid moving to edge or attacking your own body.

### `_checkCollision()`**

A helper method for `move()` to check if the snake would collide with the wall.

`::return::` : `bool` : Ture if collision happend; otherwise, False.

### `_getPosition()`**

A helper method for `move()` to get the current head position of the snake.

`::return::` : `tuple[int, int]` : (x, y)

### `detect(map : list[list[list]])` [OPTIONAL]

Detect using the map information to help your `move()`.

`::parapmeter map::` : `list[list[list]]` : 2-D list with each postion either `NONE` or a `list[int]` of `hp`
