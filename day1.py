#!/usr/bin/env python

tsum = 0
with open("day1input") as f:
    data = f.readlines()
    for line in data:
        for i in line:
            print(i)
            if i == "(":
                tsum += 1
            elif i == ")":
                tsum -= 1
print (tsum)
