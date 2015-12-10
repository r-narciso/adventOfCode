#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import permutations,groupby,product
from re import match,sub,compile
from collections import defaultdict

def day1(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
    except FileNotFoundError:
        return 'Could not find file!'
    if ab == 'a':
        return sum(1 if x == '(' else -1 for x in dat)
    if ab == 'b':
        floor = 0
        for i,x in enumerate(open(file).read(),1):
            floor += 1 if x == '(' else -1
            if floor == -1:
                return i
        return 'Never reached the basement!'

def day2(ab, file = None):
    try:
        dat = input('Text: ').splitlines() if not file else open(file).read().splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    #helper function
    def paper(s):
        s = [int(x)*int(y) for x,y in permutations(s.split('x'),2)]
        return sum(s) + min(s)
    if ab == 'a':
        return sum(paper(x) for x in dat if x)
    elif ab == 'b':
        return

def day3(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
    except FileNotFoundError:
        return 'Could not find file!'
    d = {'<':(0,-1),'>':(0,1),'^':(1,1),'v':(1,-1)}
    if ab == 'a':
        s,here = set([(0,0)]),[0,0]
        for c in dat:
            c=d[c]
            here[c[0]]+=c[1]
            s.add(tuple(here))
        return len(s)
    elif ab == 'b':
        s,here = set([(0,0)]),[[0,0],[0,0]]
        for i,c in enumerate(dat):
            c=d[c]
            here[i%2][c[0]]+=c[1]
            s.add(tuple(here[i%2]))
        return len(s)
        
def day5(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
        dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    if ab == 'a':
        #helper function
        def valid(s):
            if any(x in s for x in ['ab','cd','pq','xy']): return False #check for substring
            vowel,dup = 0,False
            for x in groupby(s):
                print(len(list(x[1])))
                if x[0] in 'aeiou': vowel += len(list(x[1]))
                if len(list(x[1])) > 1: dup = True
                if vowel>2 and dup: return True
            return False
        return len(list(filter(valid,dat)))
    elif ab == 'b':
        #helper function
        def valid(s):
            s = [s[i:i+2] for i in range(len(s))] #make bigrams
            s.pop() #remove the last item
            dup,oneSep = False, False
            for i in range(len(s)-1):
                if s[i][0] == s[i+1][-1]: oneSep = True
                if s[i] in s[i+2:]: dup = True
                if oneSep and dup: return True
            return False
        return len(list(filter(valid,dat)))

def day6(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
        dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    matcher = compile(r'(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)')
    if ab == 'a':
        operDict = {'toggle': lambda x: not x, 'turn on': lambda _: True, 'turn off': lambda _: False}
        lights_on = 0
        for line in dat:
            try:
                operator,x1,y1,x2,y2 = [int(x) if x.isdigit() else x for x in matcher.match(line).groups()]
            except (AttributeError, ValueError):
                return 'Matcher error with line:\n' + line
            for x,y in product(range(x1,x2+1),range(y1,y2+1)):
                lights[x][y],old = operDict[operator](lights[x][y]),lights[x][y]
                lights_on += lights[x][y] - old
        return lights_on
    elif ab == 'b':
        operDict = {'toggle': lambda x: x+2, 'turn on': lambda x: x+1, 'turn off': lambda x: x and x-1}
        lights_on = 0
        for line in dat:
            try:
                operator,x1,y1,x2,y2 = [int(x) if x.isdigit() else x for x in matcher.match(line).groups()]
            except (AttributeError, ValueError):
                return 'Matcher error with line:\n' + line
            for x,y in product(range(x1,x2+1),range(y1,y2+1)):
                lights[x][y],old = operDict[operator](lights[x][y]),lights[x][y]
                lights_on += lights[x][y] - old
        return lights_on
        
def day8(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
        dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    if ab == 'a':
        charSum,stringSum = 0,0
        for line in dat:
            charSum += len(line)
            stringSum += len(eval(line))
        return charSum-stringSum
    elif ab == 'b':
        charSum,stringSum = 0,0
        for line in dat:
            stringSum += len(line)
            charSum += len(sub(r'(\\|")','\\\1',line)) + 2
        return charSum-stringSum
        
from collections import defaultdict
from re import match

def day9(ab, file = None):
    MAXINT = float('Inf')
    try:
        dat = input('Text: ') if not file else open(file).read()
        dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    cities,paths = set(),defaultdict(list)
    for line in dat:
        try:
            city1,city2,time = match(r'(\w+) to (\w+) = (\d+)',line).groups()
        except (AttributeError, ValueError):
            return 'Matcher error with line:\n' + line
        cities.add(city1)
        cities.add(city2)
        paths[city1].append((int(time),city2))
        paths[city2].append((int(time),city1))
    starting = list(cities)
    def findPath(here, citiesToVisit, pathDict, pathSum = 0,visited = set()):
        if not(citiesToVisit): return pathSum #if no more cities to visit, return current path
        if not(pathDict[here]): return 0 #if there are no more paths, can't visit anymore cities
        index = 0
        visited.add(here)
        while index < len(pathDict[here]):
            there = pathDict[here][index]
            if there[1] not in visited:
                fullPath = findPath(there[1], citiesToVisit-1, pathDict, pathSum+there[0],visited)
                if fullPath:
                    visited.clear()
                    return fullPath
            index += 1
        visited.remove(here) #remove `here` from visited
        return 0
    if ab == 'a':
        for city in paths: paths[city].sort() #important
        currentMin = findPath(starting.pop(), len(cities)-1,paths) or MAXINT
        while starting:
            nextMin = findPath(starting.pop(), len(cities)-1,paths)
            currentMin = nextMin if nextMin>0 and nextMin<currentMin else currentMin
        return currentMin
    elif ab == 'b':
        for city in paths: paths[city].sort(reverse = True) #important
        currentMax = findPath(starting.pop(), len(cities)-1,paths)
        while starting:
            nextMax = findPath(starting.pop(), len(cities)-1,paths)
            currentMax = nextMax if nextMax>currentMax else currentMax
        return currentMax
    
if __name__ == '__main__':
    print(day9('a',r'C:\Users\arthurd\Documents\file.txt'))
    
        
def dayx(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
        #dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    if ab == 'a':
        return
    elif ab == 'b':
        return

def main():
    functionDict = {
        '1':day1,
        '2':day2,
        '3':day3,
        '4':day4,
        '5':day5,
        '6':day6,
        '8':day7,
        '9':day9,
    }
    while True:
        func = input('Which day would you like to do: (sample input \'1a\') ')
        if not func: break
        if func[0] in functionDict and func[1] in 'ab':
            print(functionDict[func[0]](func[1],input('Input filename: (enter nothing to use input) ')))
        else:
            print('Not valid input, please try again.')
    print('Peace out.')

if __name__ == '__main__':
    main()
