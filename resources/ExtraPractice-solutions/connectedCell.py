## Solution for 'connectedCell'
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
import math


directions =[   (-1,  0),   # left
                ( 1,  0),   # right
                ( 0, -1),   # up
                ( 0,  1),   # down
                (-1, -1),   # top-left 
                (-1,  1),   # top-right
                ( 1, -1),   # bottom-left
                ( 1,  1)    # bottom-right
            ]

def connectedCell(matrix):
    # Write your code here

    M, N = len(matrix), len(matrix[0])

    ## YES!! We can have a function inside a function
    #  This would just avoid setting GLOBAL Variables. (matrix, M, N) in this case
    def dfs(i, j):
        if (i < 0 or i >= M) or (j < 0 or j >= N):
            return 0
        if matrix[i][j] == 0:
            return 0
        ans = 1
        matrix[i][j] = 0

        for x_dir, y_dir in directions:
            ans += dfs(i + x_dir, j + y_dir)
        ''' # Alternate Way to go through directions
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ans += dfs(i + di, j + dj)
        '''
        return ans
       
    ans = 0
    for i in range(M):
        for j in range(N):
            ans = max(ans, dfs(i, j))
    return ans

def main():

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)
    print(result)