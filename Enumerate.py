# Enumerate

example = ["left" , "right", "up" , "down"]
for i in range(len(example)):
	print(i, example[i])

for i,j in enumerate(example):					#this is how we use the enumerate
	print(i,j)

example_dict = {'left':'<','right':'>','up':'^','down':'v',} 	#we use this '{}' for creating dictionaries 

[print(l,j) for l,j in enumerate(example_dict)]					#we can also use enumerate for the dictionaries
	
new_dict = dict(enumerate(example))
print(new_dict)