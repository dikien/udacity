'''
from multiprocessing import Process, Queue
import re, time

q = Queue()

def isprime(n):
    convert = ''.join('1' for i in xrange(n))
    return not re.match(r'^1?$|^(11+?)\1+$', convert)

def primeworker():
    while True:
        n = q.get()
        isprime(n)
        print time.time() - parallel_st

parallel_st = time.time()
processes = [Process(target=primeworker) for i in range(2)]
[p.start() for p in processes]
for i in range(10):
    q.put(1234567)
[p.join() for p in processes]
'''
print 1