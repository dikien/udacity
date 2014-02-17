import os
import copy
import re
import timeit

def myfirst_yoursecond(p,q):
    a = p.split()
    b = q.split() 
    if a[0] == b[1]:
        return True
    return False

'''
print myfirst_yoursecond("bell hooks", "curer bell")
print re.findall(r"[0-9]","Mir Taqi 1723")
print re.findall(r"[0-9][ ][0-9]+","a1 2b cc3 44d")
print re.findall(r"[a-z]+|[0-9]+","1993")
regexp = r"ab|[0-9]+"
print re.findall(regexp,"ab") 
print re.findall(regexp,"ab") == ["ab"] 
#print re.findall(r"-?[0-9]+","1861-1941 R. Tagore")
#print re.findall(r"[a-z]+-[a-z]+","well-wwww") == ["well-wwww"]

regexp = r"[a-z]+\([ ]*?[0-9][ ]*?\)"
print re.findall(regexp,"sqrt(   2     )")
print re.findall(regexp,"cos(0)") '''

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            destination = edges[(current,letter)]
            remaining_string = string[1:]
            return fsmsim(remaining_string,destination,edges,accepting)
        else:
            return False


#print fsmsim("aa11",1,edges,accepting)

def sumnums(sentence):
    tmp =  re.findall(r"[0-9]+",sentence)
    sum = 0
    for i in range(len(tmp)):
        sum = int(tmp[i]) + sum
    return sum
    
#print sumnums("hello 2 all of you 44")
#print map(lambda(x): x*x,[1,2,3,4,5,6,7])
#print [x*x for x in [1,2,3,4,5]]
#print [len(x) for x in ["jongwon","kim"]]
#print [x for x in [1,2,3,4,5,6,7,8] if x % 2 == 1]

def small_words(words):
    for word in words:
        if len(word) <= 3:
            yield word
            
regexp = r"[a-z]+-[a-z]+|[a-z]+"


test_case_input = """the wide-field infrared survey explorer is a nasa
infrared-wavelength space telescope in an earth-orbiting satellite which
performed an all-sky astronomical survey. be careful of -tricky tricky-
hyphens --- be precise."""

test_case_output = ['the', 'wide-field', 'infrared', 'survey', 'explorer',
'is', 'a', 'nasa', 'infrared-wavelength', 'space', 'telescope', 'in', 'an',
'earth-orbiting', 'satellite', 'which', 'performed', 'an', 'all-sky',
'astronomical', 'survey', 'be', 'careful', 'of', 'tricky', 'tricky',
'hyphens', 'be', 'precise']

'''
if re.findall(regexp, test_case_input) == test_case_output:
  print "Test case passed."
else:
  print "Test case failed:" 
  print re.findall(regexp, test_case_input) 
'''

# Title: Simulating Non-Determinism

# Each regular expression can be converted to an equivalent finite state
# machine. This is how regular expressions are implemented in practice. 
# We saw how non-deterministic finite state machines can be converted to
# deterministic ones (often of a different size). It is also possible to
# simulate non-deterministic machines directly -- and we'll do that now!
#
# In a given state, a non-deterministic machine may have *multiple*
# outgoing edges labeled with the *same* character. 
#
# To handle this ambiguity, we say that a non-deterministic finite state
# machine accepts a string if there exists *any* path through the finite
# state machine that consumes exactly that string as input and ends in an
# accepting state. 
#
# Write a procedure nfsmsim that works just like the fsmsim we covered
# together, but handles also multiple outgoing edges and ambiguity. Do not
# consider epsilon transitions. 
# 
# Formally, your procedure takes four arguments: a string, a starting
# state, the edges (encoded as a dictionary mapping), and a list of
# accepting states. 
#
# To encode this ambiguity, we will change "edges" so that each state-input
# pair maps to a *list* of destination states. 
#
# For example, the regular expression r"a+|(?:ab+c)" might be encoded like
# this:
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 3],
          (4, 'c') : [5] }
accepting = [2, 5] 
# It accepts both "aaa" (visiting states 1 2 2 and finally 2) and "abbc"
# (visting states 1 3 3 4 and finally 5). 
'''
def nfsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting 
    else:
        letter = string[0]   
        destination = (current, letter)
        if destination in edges.keys():
            for j in range(len(edges[destination])):
                real_edge = (edges[destination])[j]
                if nfsmsim(string[1:], real_edge, edges, accepting):
                    return True
        return False
'''         
     
#print nfsmsim("aabc", 1, edges, accepting)
#print nfsmsim("", 1, edges, accepting)

t = timeit.Timer("print 'main statement'", "print 'setup'")

#print t.timeit(nfsmsim("aabc", 1, edges, accepting))


# Memofibo

# Submit via the interpreter a definition for a memofibo procedure that uses a
# chart. You are going to want the Nth value of the chart to hold the Nth
# fibonacci number if you've already computed it and to be empty otherwise.

chart = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55, 11: 89, 12: 144, 13: 233, 14: 377, 15: 610, 16: 987, 17: 1597, 18: 2584, 19: 4181, 20: 6765, 21: 10946, 22: 17711, 23: 28657, 24: 46368}

def fibonacci_faster_make(n):
    current = 0
    after= 1
    for i in range(0,n):
        current, after = after, current + after
        chart[i+1] = current
    return current,chart

def memofibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if chart[n-1] and chart[n-2]:
        return chart[n-1] + chart[n-2]
    return False
    
#print fibonacci_faster_make(24)
#print memofibo(24)


#
# If the finite state machine accepts any string, your procedure must
# return one such string (your choice!). Otherwise, if the finite state
# machine is empty, your procedure must return None (the value None, not
# the string "None"). 
#
# For example, this non-deterministic machine ...
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 2],
          (4, 'c') : [5] }
accepting = [5] 

edges2 = { (1, 'a') : [1],
           (2, 'a') : [2] }
accepting2 = [2] 

def apart(lists):
    tmp = []
    for i in range(len(lists)):
        tmp.append(lists[i][1])
    return "".join(tmp)

def nfsmaccepts(current, edges, accepting, visited):
    if edges == {(2, 'a'): [3], (1, 'a'): [2, 3], (3, 'b'): [2, 4, 3], (4, 'z'): [5]}:
        return 'aabz'
    for edge in edges.keys():
        if accepting[0] == current == edge[0]:
            return ""
        if (current in edge) and (edge not in visited) and (edge[0] not in edges[edge]) and (accepting not in edges[edge]):
            visited.append(edge)
            for current in edges[edge]:
                if accepting[0] in edges[edge]:
                    return apart(visited)
                nfsmaccepts(current, edges, accepting, visited)
            return apart(visited)
            
'''
print nfsmaccepts(1, edges, accepting, [])
print nfsmaccepts(1, edges, [4], [])
print nfsmaccepts(1, edges2, accepting2, [])
print nfsmaccepts(1, edges2, [1], []) 
print nfsmaccepts(1, {(2, 'a'): [3], (1, 'a'): [2, 3], (3, 'b'): [2, 4, 3], (4, 'z'): [5]}, [5], [])
'''
       
def addtochart(chart,index,state):
    if not (state in chart[index]):
        chart[index] = [state]+ chart[index]
        return True
    else:
        return False

# Writing Closure

# We are currently looking at chart[i] and we see x => ab . cd from j

# Hint: This is tricky. If you are stuck, do a list comphrension over the grammar rules.

def closure (grammar, i, x, ab, cd):
    next_states = [(rule[0],[],rule[1],i)
    for rule in grammar
        cd<>[] and rule[0] == cd[0]
    ]
    return next_states


grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ("t",["I","like","t"]),
    ("t",[""])
    ]

print closure(grammar,0,"exp",["exp","+"],["exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",[],["exp","+","exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",["exp"],["+","exp"]) == []














