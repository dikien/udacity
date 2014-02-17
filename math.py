'''
Created on 2012. 9. 6.

@author: Administrator
'''
#import sys
#sys.path.append("C:\Users\Administrator\workspace\Python\Udacity")
#import stopwatch
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def factorial(n):
    if n == 0 :
        return 1
    if n > 0:
        n = n * factorial(n-1)
    return    
#print factorial(10)

trial = "a" * 1000

def is_palindrome1(s):
    if s == '':
        return True
    lens = len(s) - 1
    if lens%2 == 1: #even number
        i = 0
        while i < len(s)/2:
            if s[i] == s[lens - i]:
                i = i + 1
            else:
                return False
        return True
    
    if lens%2 == 0: #odd number
        i = 0
        while i < len(s)/2:
            if s[i] == s[lens - i]:
                i = i + 1
            else:
                return False
        return True        
#print time_execution('is_palindrome1(trial)')        

def is_palindrome(s): #using recursive
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
        
#print time_execution('is_palindrome(trial)') 

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_faster(n):
    current = 0
    after= 1
    for i in range(0,n):
        current, after = after, current + after
    return current

#print fibonacci_faster(20)
#print time_execution('fibonacci(30)')
#print time_execution('fibonacci_faster(30)')

def find_last(whole, part):
    last_pos = -1
    while True:
        pos = whole.find(part, last_pos+1)
        if pos == -1:
            return last_pos
        last_pos = pos

def print_multiplication_table(n):
    for i in range(n):
        for j in range(n):
            print str(i+1) + " * " + str(j+1) + " = " + str((i+1)*(j+1))

#print_multiplication_table(3)

def proc4(p):
    q=[]
    while p:
        q.append(p.pop())
    while q:
        p.append(q.pop())
    print p
    print q
        
#p=[1,2,3]
#proc4(p)

def product_list(a):
    lens = len(a)
    result = 1
    if lens == 0:
        return 1
    for i in range(lens):
        result = result * a[i]
    return result
    
#print product_list([1,2,3,4])

def bigger(a,b):
    if a > b or a ==b :
        return a
    else:
        return b
    
def greatest(a):
    lens = len(a)
    max = 0
    if lens == 0:
        return 0
    for i in range(lens):
        if a[i] > max:
            max = a[i]
    return max
    
#print greatest([4,23,1])

def total_enrollment(a):
    lens = len(a)
    tuition = 0
    students = 0
    for i in range(lens):
        students = students + a[i][1]
    for i in range(lens):
        tuition  = tuition  + a[i][2]*a[i][1]
    return students, tuition

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

#print total_enrollment(usa_univs)  

def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled

def check_sudoku(m):
    lens = len(m)
    n = 0
    whitelists = []
    for i in range(1,lens+1,1):
        whitelists.append(i)
        
    for i in range(lens):
        for j in m[i]:
            if j not in whitelists:
                return False
    
    for i in range(lens):
        if lens == len(m[i]):
            n = n + 1
    if n != lens:
        return False 

    for j in range(lens): #checking lines
        for l in range(0,lens,1):
            for k in range(0,lens,1):
                if l != k:
                    if m[j][l] == m[j][k]:
                        return False

    for j in range(lens): #checking columns
        for l in range(0,lens,1):
            for k in range(0,lens,1):
                if l != k:
                    if m[l][j] == m[k][j]:
                        return False 
    return True   

#print check_sudoku(   [[1,2,3,4,5], [2,3,1,5,6], [4,5,2,1,3], [3,4,5,2,1], [5,6,4,3,2]] )

def split_string(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char) # make a new element
                atsplit = False
            else:
                output[-1] = output[-1] + char # relay to a string
    return output
    
#out = split_string("This is a test-of the,string separation-code!"," ,!-")
#print out

def record_user_click(index,keyword,url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1] + 1

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            for element in entry[1]:
                if element[0] == url:
                    return
            entry[1].append([url,0])
            return
    index.append([keyword,[[url,0]]])

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': 
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': 
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def is_offered(courses, course, hexamester):
    res = []
    if hexamester not in courses:
        return False
    else:
        if course in courses[hexamester]:
            return True
        else:
            return False

#print is_offered(courses, 'cs101', 'apr2012')
#print is_offered(courses, 'cs003', 'apr2012')

def when_offered(courses,course):
    res = []
    for i in courses.keys():
        a =  courses[i]
        if course in a.keys():
            res.append(i)
    return res

#print when_offered (courses, 'cs101')
#print when_offered(courses, 'bio893')

def involved(courses, person):
    res = {}
    for i in courses.keys():
        a =  courses[i]
        for m in a.keys():
            if person in a[m].values():
                if i not in res:
                    res[i] = [m]
                else:
                    res[i].append(m)
    return res
                              
#print involved(courses, 'Dave')
#print involved(courses, 'Peter C.')

def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table

table = make_hashtable(10)

def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

def bucket_find(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket,key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])
        
        
def hashtable_lookup(htable, key):
    entry = bucket_find(hashtable_get_bucket(htable,key),key)
    if entry:
        return entry[1]
    else:
        return None

#hashtable_update(table, 'Python', 'Monty')
#hashtable_update(table, 'CLU', 'Barbara Liskov')
#hashtable_update(table, 'JavaScript', 'Brendan Eich')
#hashtable_update(table, 'Python', 'Guido van Rossum')
#print table
#print hashtable_lookup(table, 'Python')

