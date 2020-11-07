import argparse
import sys
import math

		
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type = float, default = 1,
                        help = "What is the value of X?")
    parser.add_argument('--n',type = float, default = 1,
                        help = "What is the value of Y?")
    parser.add_argument('--operation',type = str, default = 'exp',
                        help = "What operation do you want to perform?")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
	if args.operation == 'exp':
		return args.x**args.n
	elif args.operation == 'log':
		return math.log(args.x,args.n)
	elif args.operation == 'expm':
		return ((args.x**2)-(args.n**2))
	elif args.operation == 'exps':
		return ((args.x**2)+(args.n**2))

if __name__ == '__main__':
    main()
