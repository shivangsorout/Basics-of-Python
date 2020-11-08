# An example of generators 
'''
x = (i for i in range(600000))

print(list(x))
'''
# An example of list comprehension

x = [i for i in range(600000)]				#this is faster than the generator because this uses the memory
print(x)
