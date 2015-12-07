#!/usr/bin/env python

import re

def findInstruction(line):
    instruction = [0,[0,0],[0,0]]
    if "on" in line:
        instruction[0] = 1
    elif "toggle" in line:
        instruction[0] = 2

    m = re.search("[a-zA-Zs]*(\d+,\d+)[a-zA-Z\s]*(\d+,\d+)", line)
    coordinates = m.group(1).split(',')
    instruction[1][0] = int(coordinates[0])
    instruction[1][1] = int(coordinates[1])
    coordinates = m.group(2).split(',')
    instruction[2][0] = int(coordinates[0])
    instruction[2][1] = int(coordinates[1])
    return instruction

lightGrid = [[0 for x in range(1000)] for x in range(1000)]
lightGrid2 = [[0 for x in range(1000)] for x in range(1000)] 

with open("day6input") as f:
    lines = f.readlines()
    for line in lines:
        coordinates = findInstruction(line)
        if  coordinates[0] == 0:
            for i in range(min(coordinates[1][0],coordinates[2][0]),max(coordinates[2][0],coordinates[1][0]) + 1):
                for j in range(min(coordinates[1][1],coordinates[2][1]), max(coordinates[2][1], coordinates[1][1]) + 1):
                    lightGrid[i][j] = 0
		    lightGrid2[i][j] = lightGrid2[i][j] - 1 if lightGrid2[i][j] > 1 else 0
                    
        elif coordinates[0] == 1:
            for i in range(min(coordinates[1][0],coordinates[2][0]),max(coordinates[2][0],coordinates[1][0]) + 1):
                for j in range(min(coordinates[1][1],coordinates[2][1]), max(coordinates[2][1], coordinates[1][1]) + 1):
                    lightGrid[i][j] = 1
                    lightGrid2[i][j] += 1
        else:
            for i in range(min(coordinates[1][0],coordinates[2][0]),max(coordinates[2][0],coordinates[1][0]) + 1):
                for j in range(min(coordinates[1][1],coordinates[2][1]), max(coordinates[2][1], coordinates[1][1]) + 1):
                    lightGrid[i][j] = 1 if lightGrid[i][j] == 0 else 0
		    lightGrid2[i][j] += 2

tsum = 0
tsum2 = 0
for i in range(1000):
    for j in range(1000):
        if (lightGrid[i][j] == 1):
            tsum += 1
        tsum2 += lightGrid2[i][j]

print("First part: %d"%tsum)
print("Second part: %d"%tsum2)
