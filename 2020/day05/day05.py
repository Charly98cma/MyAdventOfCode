#!/usr/bin/python
from sys import argv as sysArgv

passes = {int(l.translate(str.maketrans('FBLR', '0101')), 2) for l in open(sysArgv[1],'r')}
print("1st STAR SOLUTION ->", max(passes))
print("2nd STAR SOLUTION ->", set(range(min(passes), max(passes))) - passes)
