import timeit as t

# An example of generators 
'''
x = (i for i in range(600000))

print(list(x))
'''
# An example of list comprehension
'''
x = [i for i in range(600000)]              #this is faster than the generator because this uses the memory
print(x)
'''

input_list = [5,7,25,15,0,6,9,10]

def div_by_f(num):
    if num % 5 == 0:
        return True
    else:
        return False
'''
x = [i for i in input_list if div_by_f(i)]  #list comprehension

print(x)
'''

x = (i for i in input_list if div_by_f(i))  #generator
print(list(x))

[[print(e,r) for r in range(4)] for e in range(6)]

print(t.timeit('''1+6''',number = 500000))  #use of timeit module

print(t.timeit('''

num = range(500)
def div_by_2(num):
    if (num/2).is_integer():
        return True
    else:
        return False
x = [i for i in num if div_by_2(i)]
 ''', number = 50000))

print(t.timeit('''

num = range(500)
def div_by_2(num):
    if (num/2).is_integer():
        return True
    else:
        return False
x = (i for i in num if div_by_2(i))
 ''', number = 50000))