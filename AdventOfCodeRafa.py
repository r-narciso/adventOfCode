#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import permutations
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


def dayx(ab, file = None):
    try:
        dat = input('Text: ') if not file else open(file).read()
    except FileNotFoundError:
        return 'Could not find file!'
    if ab == 'a':
        return
    elif ab == 'b':
        return

def main():
    functionDict = {
        '1':day1,
        '2':day2
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
