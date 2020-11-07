#String Concatenation

names = ['Joe','John','Kite','Phil']

for name in names:
    statement = " ".join(['Hello there',name])
    print(statement)

#more impactful example for this is if we have to print all the list of the names then

print(', '.join(names))