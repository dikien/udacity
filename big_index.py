import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])
    
def make_string(p):
    s = ""
    for e in p:
        s = s + e
    return s

def lookup(index,keyword):
    for i in index:
        if i[0] == keyword:
            return i[1]
    return []
  
def make_big_index(size):
    index = []
    letters = ['a','a','a','a','a','a','a','a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index,word,'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'
    return index

def bad_hash_string(keyword,buckets):
    return ord(keyword[0])%buckets

def hash_string(keyword,buckets):
    h = 0
    for c in keyword:
        h = (h + ord(c)) % buckets
    return h

def test_hash_function(func,keys,size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w,size)
            results[hv] += 1
            keys_used.append(w)
    return results

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

def hashtable_add(htable, key, value):
    hashtable_get_bucket(htable, key).append([key, value])

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return htable
    bucket.append([key, value])
        



table =  make_hashtable(3)
hashtable_add(table, 'udacity', 23)
hashtable_add(table, 'jongwon', 17)
hashtable_add(table, 'kim', 19)

print table
print hashtable_get_bucket(table, 'udacity')
print hashtable_lookup(table, 'udacity')
print hashtable_update(table, 'udacity', 27)
print hashtable_lookup(table, 'udacity')

#words = get_page('http://www.google.com').split()
#print time_execution('test_hash_function(bad_hash_string, words, 12)')
#print time_execution('test_hash_function(hash_string, words, 12)')
#counts = test_hash_function(bad_hash_string, words, 12)
#print hash_string('a',12)
#index_10 = make_big_index(10000)
#print index_10
#print time_execution('lookup(index_10,"aaaaaaaa")')