#!/usr/bin/env python


def findCoordinates(char):
        print(char)
        if char == "<":
            coordinates[1] -= 1
        elif char == ">":
            coordinates[1] += 1
        elif char == "^":
            coordinates[0] += 1
        elif char == "v":
            coordinates[0] -= 1

def findMaxSize():
    maxSize = [0,0,0,0]
    with open("day3input") as f:
        line = f.read()
        for char in line:
            if char == "<":
                maxSize[0] += 1
            elif char == ">":
                maxSize[1] += 1
            elif char == "^":
                maxSize[2] += 1
            elif char == "v":
                maxSize[3] += 1
    return max(maxSize)


maxLength = findMaxSize()
print(maxLength)
coordinates = [0,0]
location = [[0 for x in range(-maxLength - 1, maxLength + 1)] for x in range(-maxLength - 1, maxLength + 1)]
with open("day3input") as f:
    line = f.read()
    print(line)
    location[0][0] += 1
    for char in line:
        if char == "\n":
            print("end of file")
            break
        findCoordinates(char)
        print("coordinates[0] : %d, coordinates[1] : %d"%(coordinates[0],coordinates[1]))
        location[coordinates[0]][coordinates[1]] += 1
tsum = 0
for i in range(-maxLength - 1, maxLength + 1):
    for j in range(-maxLength - 1, maxLength + 1):
        if location[i][j] > 0:
            tsum += 1
print(tsum)
