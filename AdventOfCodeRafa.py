#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import permutations,groupby,product
from re import match,sub,compile
from collections import defaultdict
from json import load

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
        
def day9(ab, file = None):
    MAXINT = float('Inf') if ab == 'a' else 0
    try:
        dat = input('Text: ') if not file else open(file).read()
        dat = dat.splitlines()
    except:
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
    def findPath(here, citiesToVisit, pathSum = 0,visited = set()):
        if not(citiesToVisit): return pathSum #if no more cities to visit, return current path
        if not(paths[here]): return MAXINT #if there are no more paths, can't visit anymore cities
        visited.add(here)
        for distance, name in paths[here]:
            if name not in visited:
                fullPath = findPath(name, citiesToVisit-1, pathSum+distance,visited)
                if fullPath:
                    visited.clear()
                    return fullPath
        visited.remove(here)
        return MAXINT
    if ab == 'a':
        for city in paths: paths[city].sort() #important
        return min(findPath(c, len(cities)-1) for c in cities)
    elif ab == 'b':
        for city in paths: paths[city].sort(reverse = True) #important
        return max(findPath(c,len(cities)-1) for c in cities)
        
def day10(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
        #dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    if ab == 'a':
        for _ in range(40):
            dat = ''.join(str(len(list(j)))+i for i,j in groupby(dat))
        return len(dat)
    elif ab == 'b':
        for _ in range(50):
            dat = ''.join(str(len(list(j)))+i for i,j in groupby(dat))
        return len(dat)
            
def day11(ab, file = None):
    try:
        data = input('Text: ') if not file else open(file).read()
        #dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    def getPass(dat):
        def getNext(s, forbidden = {8,11,14}):
            new,remainder = [],0
            while s:
                new.append((s.pop(0)+1)%26)
                new[-1] += new[-1] in forbidden
                if new[-1]:
                    new.extend(s)
                    return new
            return new
        dat = [ord(c)-97 for c in dat.strip().lower()]
        found,temp = False,[]
        while dat:
            temp.append(dat.pop(0))
            if temp[-1] in [8,11,14]:
                temp[-1] += 1
                for _ in dat:
                    temp.append(0)
                break
        dat = getNext(temp[::-1])
        while True:
            dup,chain = 0,[0,dat[0]+1]
            for i,x in enumerate(groupby(dat)):
                if len(list(x[1]))>1:
                    dup += 1
                    if chain[0] == 1: chain[1] = x[0]
                chain[0] += 1 if (chain[1] - 1 == x[0] or chain[0] > 2) else -chain[0] + 1
                chain[1] = x[0]
                if dup > 1 and chain[0] > 2:
                    return ''.join([chr(x+97) for x in dat[::-1]])
            dat = getNext(dat)
    if ab == 'a':
        return getPass(data)
    elif ab == 'b':
        return getPass(getPass(data))
        
def day12(ab, file = None):
    
    if ab == 'a':
        def SmartSum(x):
            if isinstance(x,int):
                return x
            elif isinstance(x, list):
                return sum([SmartSum(i) for i in x])
            elif isinstance(x, dict):
                return sum([SmartSum(x[i]) for i in x])
            else:
                return 0
        try:
            return SmartSum(load(open(file)))
        except FileNotFoundError:
            return 'Could not find file!'
    elif ab == 'b':
        def SmartSum(x):
            if isinstance(x,int):
                return x
            elif isinstance(x, list):
                return sum([SmartSum(i) for i in x])
            elif isinstance(x, dict):
                if 'red' in x.values(): return 0
                return sum([SmartSum(x[i]) for i in x])
            else:
                return 0
        try:
            return SmartSum(load(open(file)))
        except FileNotFoundError:
            return 'Could not find file!'
    
    def day13(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
        dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    people,happy = set() if ab == 'a' else set(('me',)),defaultdict(int)
    for line in dat:
        try:
            name1, gorl, num, name2 = match(r'(\w+) would (gain|lose) (\d+) (?:\w+ )*(\w+).',line).groups()
        except (AttributeError, ValueError):
            return 'Matcher error with line:\n' + line
        people.add(name1)
        people.add(name2)
        happy[tuple(sorted((name1,name2)))]+= int(num) if gorl == 'gain' else -int(num)
    def rotations(rotator,howMany):
        return [rotator[i:]+rotator[:i] for i in range(howMany)]
    l = [arrangement for arrangement in zip(*rotations(list(people),len(people)))]
    optimal = 0
    for arrangement in permutations(people):
        optimal = max(optimal,sum(happy[tuple(sorted((x,y)))] for x,y in zip(*rotations(arrangement,2))))
    return optimal

def day14(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
        dat = dat.splitlines()
    except FileNotFoundError:
        return 'Could not find file!'
    distance, time = {}, 2503
    if ab == 'a':
        for line in dat:
            name, speed, length, rest =[int(x) if x.isdigit() else x for x in match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.',line).groups()]
            distance[name] = speed * (length *(time // (length + rest)) + length % (time % (length + rest)))
        return max(distance.values())
    elif ab == 'b':
        stats,points = {' ':[0]}, {}
        winning = ' '
        for line in dat:
            name, speed, length, rest =[int(x) if x.isdigit() else x for x in match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.',line).groups()]
            stats[name] = [speed,length,length+rest]
            distance[name],points[name] = 0,0
            if speed > stats[winning][0]: winning = name
        for i in range(time):
            for name in distance:
                distance[name] += stats[name][0] if i%stats[name][-1] < stats[name][1] else 0
                if distance[name] > distance[winning]: winning = name
            points[winning] += 1
        return points, sum(points.values())


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
        '10':day10,
        '11':day11,
        '12':day12,
        '13':day13,
        '14':day14
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
