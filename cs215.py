import os
import math
import itertools


def naive(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if z == 84:
            print y
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z

# when x = 7, z = 84 --> y = ?
#print russian(63, 12)


def rec_naive(a,b):
    if a == 0:
        return 0
    return b + rec_naive(a-1, b)

#print rec_naive(17,6)
#Bit Shift
#print 17 >> 1

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y



# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    orderings = list(itertools.permutations(graph))
    for ordering in orderings:
        score = []
        for i in range(len(ordering)-1):
            if ordering[i][1] == ordering[i+1][0]:
                score.append(0)
        if ordering[0][0] == ordering[-1][1]:
                score.append(0)
        if len(score) == len(ordering):
            return ordering


#print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

G = {}

n = 256
side = int(math.sqrt(n))

for i in range(side):
    for j in range(side):
        if i < side-1: make_link(G, (i,j), (i+j,j))
        if j < side-1: make_link(G, (i,j), (i,j+1))
        
print len(G)

print sum([len(G[node]) for node in G.keys()])/2