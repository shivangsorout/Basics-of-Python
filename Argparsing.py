import argparse
import sys
import math

def calc(x,n,op):
	if op == 'exp':
		return x**n
	elif op == 'log':
		return math.log(x,n)
	elif op == 'expm':
		return ((x**2)-(n**2))
	elif op == 'exps':
		return ((x**2)+(n**2))
		
oper = calc(9,3,'exps')
print(oper)	
