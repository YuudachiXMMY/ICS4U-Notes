## Slow Solution
def gridlandMetro(n, m, k, track):

    matrix = [ [0 for _ in range(m)] for _ in range(n)]

    for row in track:
        r = row[0] - 1
        c1 = row[1] - 1
        c2 = row [2] - 1
        for i in range(c1, c2+1):
            matrix[r][i] += 1

    count = 0
    for row in matrix:
        for item in row:
            if item == 0:
                count += 1

    return count

def main():
    n, m, k = map(int, input().split())

    track = []

    for _ in range(k):
        r, c1, c2 = map(int, input().split())
        track.append([r, c1, c2])

    res = gridlandMetro(n, m, k, track)
    print(res)