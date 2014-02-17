import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1

#print time_execution('1+1')[1]

def proc1(input_list):
    maximum = None
    for element in input_list :
        if maximum < element:
            maximum = element
    return maximum

def proc2(input_list):
    sum = 0
    while len(input_list) > 0:
        sum = sum + input_list[0]   # Assume input_list[0] is constant time
        input_list = input_list[1:]  # Assume input_list[1:] is constant time
    return sum

def proc3(input_list):
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i] == input_list[j] and i != j:
                return False
    return True

def make_list(m):
    e = []
    for i in range(m):
        e.append(i)
    return e

a = make_list(1000)
b = make_list(2000)
c = make_list(3000)
d = make_list(4000)
e = make_list(5000)
 
print time_execution('proc1(a)')
print time_execution('proc1(b)')
print time_execution('proc1(c)')
print time_execution('proc1(d)')
print time_execution('proc1(e)')

print time_execution('proc2(a)')
print time_execution('proc2(b)')
print time_execution('proc2(c)')
print time_execution('proc2(d)')
print time_execution('proc2(e)')

print time_execution('proc3(a)')
print time_execution('proc3(b)')
print time_execution('proc3(c)')
print time_execution('proc3(d)')
print time_execution('proc3(e)')

