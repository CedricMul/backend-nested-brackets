#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys


def is_nested(line):
    nest = line.split('')
    i = 0
    while i < len(nest):
        if (nest[i] == '(') and (nest[i + 1] == '*'):
            starSlice = nest[i + 1:]
            if '*' in starSlice and starSlice[starSlice.index('*') + 1] == ')':
                nest[i] = ''
                nest[i+1] = ''
                nest[i + 1 + starSlice.index('*')] = ''
                nest[i + 2 + starSlice.index('*')] = ''
        if nest[i] == '(':
            parSlice = nest[i+1:]
            if ')' in parSlice and (parSlice[parSlice.index(')') - 1] != '*'):
                nest[i] = ''
                nest[i + 1 + starSlice.index(')')] = ''
        if nest[i] == '<':
            anSlice = nest[i+1:]
            if '>' in anSlice:
                nest[i] = ''
                nest[i+1 + anSlice.index('>')]
        if nest[i] == '[':
            sqSlice = nest[i+1:]
            if ']' in sqSlice:
                nest[i] = ''
                nest[i + 1 + sqSlice.index(']')] = ''
        if nest[i] == '{':
            brSlice = nest[i+1:]
            if '}' in brSlice:
                nest[i] = ''
                nest[i+1 + brSlice.index('}')] = ''
    if '(' in nest:
        return ('No', nest.index('('))
    elif '[' in nest:
        return ('No', nest.index('['))
    elif '{' in nest:
        return ('No', nest.index('{'))
    elif '<' in nest:
        return ('No', nest.index('<'))
    elif '>' in nest:
        return ('No', nest.index('>'))
    elif '}' in nest:
        return ('No', nest.index('}'))
    elif ']' in nest:
        return ('No', nest.index(']'))
    elif ')' in nest:
        return ('No', nest.index(')'))
    else:
        return 'Yes'



def main(args):
    c = 0
    num = 0
    lineList = []
    with open (args, 'r') as f:
        for line in f:
            num += 1
        while c < num:
            lineList.append(is_nested(f.readLine()))
            print(lineList[c])
            c += 1
    f.close()
    w = open('output.txt', 'a')
    for l in lineList:
        w.write(l)
    w.close()





if __name__ == '__main__':
    main(sys.argv[1:])
