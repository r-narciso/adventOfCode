#!/usr/bin/env python

def isNice(word):
    vowelCount = 0
    hasDuplicate = False
    prev = '';
    for i in word:
        if prev == i:
            hasDuplicate = True
        prev = i
        if isVowel(i):
            vowelCount += 1
    if hasDuplicate and vowelCount >= 3:
        return True
    else:
        return False

def isVowel(char):
    if char == "a" or char == "e" or char == "i" or char == "u" or char == "o":
        return True
    else:
        return False

with open("day5input") as f:
    count = 0
    lines = f.readlines()
    for i in lines:
        if(isNice(i) and "ab" not in i and "cd" not in i and "pq" not in i and "xy" not in i):
            count += 1
print("First part total is : %d"%count)

def hasRepeat(word):
    for i in range(0, len(word) - 2):
        if word[i] == word[i+2]:
            return True
    return False

def hasTwoLetterNotOverlapping(word):
    for i in range(0, len(word) - 2):
        if word[i]+word[i+1] in word[i+2:]:
            return True
    return False

count = 0

with open("day5input") as f:
    lines = f.readlines()
    for line in lines:
        if hasRepeat(line) and hasTwoLetterNotOverlapping(line):
            count += 1
print("Second part total is : %d"%count)
    
