import os, time, random

# Size of the maze and Counter for Path Looking
rowN = 0
colN = 0
counter = 0

#2D list of the maze layout
maze = []

# Display maze
def displayMaze():
    global maze

    #Slow down to watch simulation
    # time.sleep(0.1)
    os.system("cls")

    #Adjust output to make it look better on the screen
    map = "\n\n"
    for row in range(0,len(maze)):
        for col in range(0,len(maze[row])):
            if maze[row][col] == "1":
                map = map + "[X]"

            if maze[row][col] == "0":
                map = map +  "   "

            if maze[row][col] == ".":
                map = map + " . "

            if maze[row][col] == "2":
                map = map + "   "

            if maze[row][col] == "E":
                map = map + " E "

            if maze[row][col] == "S":
                map = map + " S "

        map = map + "\n"

    print(map)

# Read user Input for maze size.
def userInput():
    global rowN, colN, counter

    rowN = int(input("Enter the number of rows: "))
    while rowN < 4:
        print("ERROR: Invalid Row Number input!")
        rowN = int(input("Re-Enter the number of rows: "))

    colN = int(input("Enter the number of cols: "))
    while colN < 4:
        print("ERROR: Invalid Col Number input!")
        colN = int(input("Re-Enter the number of cols: "))

    counter = int(input("Enter the Moves: "))
    while counter < 2:
        print("ERROR: Invalid Moves Number input!")
        counter = int(input("Re-Enter the Moves: "))

# Move through the maze. While moving, break the walls `1`.
def move(row,col):
    global maze, counter
    rowMove = row
    colMove = col
    for i in range(0, counter):
        displayMaze()
        if i == counter - 1:
            maze[rowMove][colMove] = "E"
            displayMaze()
            return True
        # Break Current Wall
        else:
            
            if maze[rowMove][colMove] == "1":
                #Mark path as open
                maze[rowMove][colMove] = "0"
            else:
                i += 1

            # Random Move 
            # Right and Down have a greater possibility 
            possibles = [[rowMove,colMove+1],[rowMove,colMove+1],[rowMove,colMove-1],[rowMove+1,colMove],[rowMove+1,colMove],[rowMove+1,colMove]]
            
            moveDir = random.choice(possibles)
            rowMove = moveDir[0]
            colMove = moveDir[1]

            while (rowMove >= rowN - 1 or rowMove < 0 or colMove >= colN - 1 or colMove < 0) and \
                  (maze[rowMove][colMove] != "0" or maze[rowMove][colMove] != "s"):
                moveDir = random.choice(possibles)
                rowMove = moveDir[0]
                colMove = moveDir[1]
    return False

# Initialize the Maze with a starting position `S`
def initializeMaze(row, col):
    global maze

    # Initilize a matrix of rowN x coln with `1`
    maze = [[ "1" for i in range(col) ] for j in range(row)]

    # Randomly Generate a starting position `S` at the top-left quartile
    yPos = random.randint(1, len(maze)//4)
    xPos = random.randint(1, len(maze[0])//4)

    maze[yPos][xPos] = "S"

    move(yPos, xPos)

    return maze

# Save the Matrix to a Text file
def writeMatrix(matrix, fileName="./Unit 2/maze/randomMaze.txt"):
    with open(fileName, 'w') as file:
        for row in matrix:
            file.write(','.join([str(item) for item in row]))
            file.write('\n')

# Random fill the Maze with `0`
def randomFill():
    global maze

    n = ((rowN * colN) - counter) // 3

    while n != 0:
        randrow = random.randint(1, rowN-1)
        randcol = random.randint(1, colN-1)
        if maze[randrow][randcol] == "1":
            maze[randrow][randcol] = "0"
            n -= 1 
    displayMaze()

def main():
    
    # Get Maze Size from user
    userInput()
    
    # 1. Initialize a Maze with all `1` and a starting position `S`
    # 2. Move to break the walls `1`
    initializeMaze(rowN, colN)

    # Random break some walls:
    #   randomly change `1` to `0`
    randomFill()

    # Save Maze to a text file
    writeMatrix(maze)

#Start the program
main()