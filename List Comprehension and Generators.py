# An example of generators 
'''
x = (i for i in range(600000))

print(list(x))
'''
# An example of list comprehension
'''
x = [i for i in range(600000)]				#this is faster than the generator because this uses the memory
print(x)
'''

input_list = [5,7,25,15,0,6,9,10]

def div_by_f(num):
	if num % 5 == 0:
		return True
	else:
		return False

x = [i for i in input_list if div_by_f(i)]

print(x)
