def parseData(file="mine.txt"):
    with open(file, 'r') as f:
        data = [line.rstrip('\n').replace(".", "0").split() for line in f]

    # convert 0 to interger
    data = [[int(x) if x.isdigit() else x for x in row] for row in data]
    return data

mydata = parseData()
print(mydata)
