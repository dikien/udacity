# -*- coding: UTF-8 -*-
from __future__ import division
import os
import copy
import re
import timeit
import math
import itertools
import time
import string
import cProfile


houses = [1,2,3,4,5]
orderings = list(itertools.permutations(houses))

def imright(h1, h2):
    return h1-h2 ==1

def nextto(h1, h2):
    return abs(h1-h2) == 1

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

#print zebra_puzzle()

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        time = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])    
    return min(times), average(times), max(times)

def timecall(fn):
    t0 = time.clock()
    result = fn
    t1 = time.clock()
    return t1-t0, result

def timecalls(n, fn):
    if isinstance(n, int):
        times = [timecall(fn)[0] for _ in range(n)]
    else:
        time = []
        while sum(times) < n:
            times.append(timecall(fn)[0])    
    return min(times), average(times), max(times)





'''
for (red, green, ivory, yellow, blue) in orderings:
    for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings:
        for (dog, snails, fox, horse, ZEBRA) in orderings:
            for (coffee, tea, milk, oj, WATER) in orderings:
                for (OldGold, kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                    if (Englishman is red):

def sq(x): print 'sq called', x; return x * x
g = (sq(x) for x in range(10) if x%2 == 0)
print g
print next(g)
print next(g)
print next(g)
print next(g)
print list((sq(x) for x in range(10) if x%2 == 0))    


def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1

def all_ints():
    yield 0
    for i in ints(1):
        yield +i
        yield -i
        
print list(all_ints())'''

'''
items = ["red"]
it = iter(items)
try:
    while True:
        x = next(it)
        print x
except StopIteration:
    pass
'''

# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????. 

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLOTO not in set([PLANETS])""".splitlines()


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f
    
def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]',formula)))
    for digits in itertools.permutations('0123456789', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def test():
    t0 = time.clock()
    for example in examples:
        print; print 13*' ', example
        print '%6.4f sec:  %s ' % timedcall(solve, example)
    print '%6.4f tot.' % (time.clock()-t0)

#cProfile.run('test()')

f = lambda Y, M, E, U, O:(1*U+10*O+100*Y) == (1*E+10*M)**2
#print f
#print f(1,2,3,4,5)
#print f(2,1,7,9,8) 

def compile_word(word):
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                 for (i,d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

#print compile_word('YOU')

#print '%(language)s has %(#)03d quote types.' % {'language': "Python", "#":2}

def gen_num():
    j = 0
    while 1:
        yield j
        j = j + 1
 
a = gen_num()
#print a.next()


# Hopper does not live on the top floor. ok
# Kay does not live on the bottom floor. ok
# Liskov does not live on either the top or the bottom floor.ok 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. ok
# Liskov does not live on a floor adjacent to Kay's. ok
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.


def floor_puzzle1():
    apts = first, _, middle, _, _ = [1, 2, 3 ,4 ,5]
    floors = list(itertools.permutations(apts))
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for [Hopper, Kay, Liskov, Perlis, Ritchie] in floors
                if Hopper is not 5 and Kay is not 1
                if Liskov is not 1
                if Liskov is not 5
                if not nextto(Ritchie,Liskov)
                if not nextto(Kay,Liskov)
                if Perlis - Kay >= 1
                )

def floor_puzzle2():
    apts = first, _, middle, _, _ = [1, 2, 3 ,4 ,5]
    floors = list(itertools.permutations(apts))
    for [Hopper, Kay, Liskov, Perlis, Ritchie] in floors:
        if Hopper is not 5 and Kay is not 1:
            if Liskov is not 1:
                if Liskov is not 5:
                    if not nextto(Ritchie,Liskov):
                        if not nextto(Kay,Liskov):
                            if Perlis - Kay >= 1:
                                return [Hopper, Kay, Liskov, Perlis, Ritchie]


#print timecall(floor_puzzle())                  
#print timecalls(5,floor_puzzle1())              
#print timecalls(5,floor_puzzle2())              
                
                
                    
    
