import os, time, random

#2D list of the maze layout
maze = []

#2D list of the path taken [row,col] coordinates
path = []


#Print maze
def displayMaze():

    #Slow down to watch simulation
    time.sleep(0.2)
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

#Move through the maze
def move(row,col):

    global path
    global maze


    #Possible Movements
    possibles = [[row,col+1],[row,col-1],[row-1,col],[row+1,col]]

    #Randomize direction choice so it doesn't favor 1 direction over another
    random.shuffle(possibles)


    #Move along the open paths
    if maze[row][col] == "0" or maze[row][col] == "S":

        #Mark path as open
        maze[row][col] = "."
        path.append([row,col])
        displayMaze()

        #Move in next possible direction
        if (move(possibles[0][0],possibles[0][1])):
            return True

        elif (move(possibles[1][0],possibles[1][1])):
            return True

        elif (move(possibles[2][0],possibles[2][1])):
            return True

        elif (move(possibles[3][0],possibles[3][1])):
            return True

        #Mark path as dead end and backtrack
        else:
            maze[row][col] = "2"
            path.remove([row,col])
            displayMaze()
            return False

    #Found exit
    elif maze[row][col] == "E":
        maze[row][col] = "."
        path.append([row,col])
        return True

    return False

def main():
    os.system("cls")

    # Store the maze in a 2D list
    global maze
    file = open("MazeSearchFile.txt", "r")
    while True:
        line = file.readline()
        if line == "":
            break
        else:
            values = line.rstrip("\n").split(",")
            maze.append(values)

    #Find the starting position
    for row in range(0,len(maze)):
        for col in range(0,len(maze[row])):
            if maze[row][col] == "S":
                startRow = row
                startCol = col
                break

    #Make the first move
    move(startRow,startCol)

    #Maze Solved
    displayMaze()
    print("A Solution:")
    print(path)

#Start the program
main()