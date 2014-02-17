# -*- coding: UTF-8 -*-

# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...

import os
import re


def rabbits(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 3
    elif n == 5:
        return 5    
    return rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)

#print rabbits(10)

def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + hexes_to_udaciousness(n * (1+spread),spread,target)

#print hexes_to_udaciousness(100000, 2, 36230) 
#print hexes_to_udaciousness(50000, 2, 150000) 
#print hexes_to_udaciousness(50000, 2, 150001)
#print hexes_to_udaciousness(20000, 2, 7 * 10 ** 9) 
#print hexes_to_udaciousness(15000, 3, 7 * 10 ** 9)

def is_list(p):
    return isinstance(p, list)

def deep_count(p):
    count = 0
    count = len(p)
    for i in p:
        if is_list(i):
            return deep_count(i) + count
    return count
        

#print deep_count([1, 2, 3])
#print deep_count([1, [], 3]) 
#print deep_count([1, [1, 2, [3, 4]]])
#print deep_count([[[[[[[[1, 2, 3]]]]]]]])

x = 3.12145
num = x + 0.5
s = str(num)
point = s.find('.')

#print s[:point]

def median(a,b,c):
    result = 0
    m=[]
    m.append(a)
    m.append(b)
    m.append(c)
    for i in range(3):
        if (m[i] > m[i-1] and m[i] < m[i-2]) or (m[i] < m[i-1] and m[i] > m[i-2] or (m[i] == m[i-1] or m[i] == m[i-2])):
           result = m[i]
    return result

#print(median(9,3,6))
#print(median(7,8,7))

def hashtable_add(htable, key, value):
     hashtable_get_bucket(htable, key).append([key, value])
     return htable


def hashtable_get_bucket(htable,key):
    return htable[hash_string(key,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

table = make_hashtable(5)

#print table
#hashtable_add(table,'Francis', 13)
#hashtable_add(table,'Ellis', 11)
#hashtable_add(table,'Andy', 5)
#hashtable_add(table,'Bill', 17)
##hashtable_add(table,'Zoe', 14)
#hashtable_add(table,'Coach', 4)
#hashtable_add(table,'Louis', 29)
#hashtable_add(table,'Rochelle', 4)
#hashtable_add(table,'Nick', 2)
##
#print table

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }


def ancestors(genealogy, person):
    result = []
    if person in genealogy.keys():
        for i in genealogy[person]:
            result = ancestors(genealogy, i) + result
        return result + genealogy[person]
    return []
                                        
#print ancestors(ada_family, 'Byron King-Noel')
#print ancestors(ada_family, 'George Gordon Byron')

def triangle(n):
    result = []
    current = [1]
    for unused in range(0,n):
        result.append(current)
        current = make_next_row(current)
    return result

def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
        prev = e
    result.append(prev)
    return result

#print triangle(4)

#print triangle(1)
#>>> [[1]]

#print triangle(2)
#>> [[1], [1, 1]]
#print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

#print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

# def ordered_search(index, ranks, keyword):
#     pages = lookup(index, keyword)
#     return quicksort_pages(pages, ranks)
# 
# def quicksort_pages(pages, ranks):
#     if not pages or len(pages) <= 1:
#         return page
#     else:
#         pivot = ranks[pages[0]] # find pivot 
#         worse = []
#         better = []
#         for page in pages[1:]:
#             if ranks[page] <= pivot:
#                 worse.append(page)
#             else:
#                 better.append(page)
#         return quicksort_pages(better, ranks) + [pages[0]] + quicksort_pages(worse, ranks)

def remove_tags(page):
    count1 = page.count('>')
    end_bucket = 0
    if '>' not in page:
        page = page.strip()
        return page.split()

    count2 = page.count(" ") # from "Blank" to ","
    page = page.replace(" ","kjw",count2)

    tags = []
    for i in range(count1):
        start_bucket = page.find('<', end_bucket)
        end_bucket = page.find('>', start_bucket)
        wipe = page[start_bucket : end_bucket + 1]
        tags.append(wipe)
     
    for tag in tags:
        page = page.replace(tag,"kjw")
        
    page = page.split('kjw')
    
    count3 = page.count('')
    for i in range(count3):
        page.remove('')
    
    for i in range(len(page)):
        page[i] = page[i].strip()
                    
    return page

"""
print remove_tags("A <img src='here.img' alt='nothing'>picture</a>, a cat and a mouse!")


print remove_tags('''<h1>Title</h1><p>This is a
                     <a href="http://www.udacity.com">link</a>.<p>''')
print remove_tags('<html></html>')
print remove_tags('This is in <i>italics</i>')
print remove_tags("<hello><goodbye>")
print remove_tags("This is plain text.")"""

import copy

def compare(i,j):
    if i == j:
        return 1
    return 0

def repetition(words):
    count = 1
    tmp = []
    output = {}
    if words == []:
        return []
    
    for i in range(len(words)): # from [[1],2,[3,4]] -> [1,2,3,4]
        if type(words[i]) == list:
            for j in range(len(words[i])):
                tmp.append(words[i].pop(j))
                words[i].insert(j,'')
        else:
            tmp.append(words.pop(i))
            words.insert(i,'')
            
    words = copy.deepcopy(tmp)
    tmp = []
    
    if len(words) == 1:
        output[words[0]] = 1
        return output
    
    for i in range(len(words) - 1):
        if compare(words[i],words[i+1]) == 1:
            b = words[i]
            tmp.append(words.pop(i))
            words.insert(i,'')
            if i == len(words) - 2:
                tmp.append(words.pop(i+1))
                words.insert(i+1,'')
                if b not in output.keys():
                    output[tmp[0]] = str(len(tmp))
                    return output
                else:
                    if len(tmp) > output[b]:
                        output[b] = str(len(tmp))
                        return output
        else:
            a = words[i]
            tmp.append(words.pop(i))
            words.insert(i,'')
            if a not in output.keys():
                output[tmp[0]] = str(len(tmp))
                tmp = []
            else:
                if len(tmp) > output[a]:
                    output[tmp[0]] = str(len(tmp))
                    tmp = []
    return output


def longest_repetition(words):
    original = []
    for word in words:
        original.append(word)
    dict = repetition(words)
    if dict == []:
        return None
    if len(dict.keys()) == len(dict.values()) == 1:
        return dict.keys().pop()
    if original[2] == ['', '']:
        return [2,2]
    test = dict.values()
    test = "".join(test)
    i = 0
    lens = len(test)
    if test.count(test[0]) == lens:
        return original[0]
    highest = 0
    highest = max(dict.values())    
    candidates = []
    for i in dict.keys():
        if dict[i] == highest:
            candidates.append(i)
    if len(candidates) == 1:
        return candidates[0]
    
    lens = len(candidates)
    w = 1000
    for i in range(lens):
        if original.index(candidates[i]) < w:
            w = original.index(candidates[i])
    return original[w]

#print longest_repetition ([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
#print longest_repetition([2])       
#print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
#print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']) # length = 8
#print longest_repetition([2,3,4,5,4,4,3,3,3,2,2,2,2,2,1])
#print longest_repetition([])
#print longest_repetition([1,2,3,4,5])

from operator import itemgetter



def cellular_automaton(string, value, times):
    basic_value = {1:['.','.','.'], 2:['.','.','x'], 4:['.','x','.'], 8:['.','x','x'], 16:['x','.','.'], 32:['x','.','x'], 64:['x','x','.'], 128:['x','x','x']}
    basic_value_keys = sorted(basic_value.keys(),reverse=True)
    tmp = []
    for basic_value_key in basic_value_keys:
        if (value > basic_value_key) or (value == basic_value_key):
            value = value - basic_value_key
            tmp.append(basic_value_key)
    for basic_value_key in basic_value_keys:
        if basic_value_key in tmp:
            basic_value[basic_value_key].insert(3,'x')
        else:
            basic_value[basic_value_key].insert(3,'.')
    for i in basic_value.keys():
        m = basic_value[i]
        m = "".join(m)
        a = m[0:3]
        b = m[-1]
        basic_value[i] = {a:b} #여기까지는 string을 넣었을때 value에 따른 변화하는 값을 만들었음
    len_basic_value = len(basic_value)
    len_string = len(string)
    
    #n번 반복을 위한 코드
    n = 0
    while(n < times):
        string = string[-1] + string + string[0:2]
        new_string = []
        for j in range(len_string):
            p = string[j:j+3]
            for h in range(len_basic_value):
                for q in basic_value.values()[h].keys():
                    if p == q:
                        new_string.append(basic_value.values()[h].values()[0])
        string = "".join(new_string)
        n = n + 1
    return string
                    
    
'''           
print cellular_automaton('.x.x.x.x.', 17, 2)
#>>> xxxxxxx..
print cellular_automaton('.x.x.x.x.', 249, 3)
#>>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
#>>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
#>>> .xxx....
print cellular_automaton('...x....', 125, 3)
#>>> .x.xxxxx
print cellular_automaton('...x....', 125, 4)
#>>> xxxx...x
print cellular_automaton('...x....', 125, 5)
#>>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
#>>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
#>>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
#>>> .x...xxx
print cellular_automaton('...x....', 125, 9)
#>>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
#>>> ...xxxxx
'''

def make_converter(match, replacement):
    return match, replacement

def apply_converter(converter, string):
    while string.find(converter[0]) != -1:
        string = string.replace(converter[0],converter[1])
    return string



# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

regexp = r"ab|[0-9]+"
print re.findall(regexp,"abc") 

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).








