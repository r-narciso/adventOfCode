#!/usr/bin/env python

with open("/home/ccatt/Documents/programming/python/adventOfCode/day2input.txt") as f:
	tsum = 0
	data = f.readlines()
	for i in data:
		line = i.replace("\n","").split('x')
		for i in range(0,len(line)):
			line[i] = int(line[i])
		lowest = line[0] * line[1]
		if (line[0] * line[2]) < lowest:
		    lowest = line[0] * line[2];
		if line[1] * line[2] < lowest:
		    lowest = line[1] * line[2];
		tsum += lowest + 2*(line[0] * line[1] + line[0] * line[2] + line[1] * line[2]);lowest = (line[0]*line[1])
