
myData = [
            [99,42,74,83,100],
            [90,91,72,88,95],
	        [88,61,74,89,96],
	        [61,89,82,98,93],
	        [93,73,75,78,99],
	        [50,65,92,87,94],
	        [43,98,78,56,99]
        ]
def printM(matrix):
    print("[")
    for row in matrix:
        print(row)
    print("]")
# Rectangular Matrix: M x N matrix 
M = 5  # Row Size
N = 5  # Col Size

myMatrix = []
for row in range(M):
    currentRow = []
    for col in range(N):
        currentRow.append(0)
    # currentRow = [0,0,0,0,0]
    myMatrix.append(currentRow) 
printM(myMatrix)

for r in range(len(myMatrix)):
    for c in range(len(myMatrix[0])):
        if r%2 == 0 and c%2 == 0:              
            myMatrix[r][c] = 1  
        if r%2 == 1 and c%2 == 1:
            myMatrix[r][c] = 1
printM(myMatrix)
# initializing 
myMatrix2 = []
for r in range(M):
    currentRow = []
    for c in range(N):
        if r%2 == 0 and c%2 == 0:
            currentRow.append(1)
        elif r%2 == 1 and c%2 == 1:
            currentRow.append(1)
        else: 
            currentRow.append(0)
    myMatrix2.append(currentRow)
printM(myMatrix2)
target = 99
coordinates = []

# Nested Loop: Left to Right then Top to Down 
for row in range(M):
    for col in range(N):
        if myData[row][col] == target: 
            position = [row,col] # (x , y)
            coordinates.append(position)
print(coordinates)
        
