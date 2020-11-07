#String Concatenation
import os

names = ['Joe','John','Kite','Phil']

for name in names:
    statement = " ".join(['Hello there',name])
    print(statement)

#more impactful example for this is if we have to print all the list of the names then

print(', '.join(names))


#using .join for file paths

location_of_file = 'I:\\Python\\Basics-of-Python'
filename = 'String Concatenation and formatting intermediate.py'
with open(os.path.join(location_of_file,filename)) as f:
    print(f.read())


#String formatting like ______ bought ______ apples today!

who = "Nobita"
how_many = 12

print('\n{} bought {} apples today!'.format(who,how_many))