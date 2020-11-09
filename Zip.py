x = [1,2,3,4,5,6]

y = [5,65,3,5,3,2]

z = [9,7,6,4,3,2]

'''
for i,j in zip(x,y):
    print(i,j)

for i in zip(x,y):
    print(i)

for i,j,k in zip(x,y,z):
    print(i,j,k)



print(zip(x,y,z))               #showing that zip fuction creates a zip object

print(list(zip(x,y,z)))         #we can convert zip into list

name = ['Jenny', 'Lilly', 'Peter', 'John']
num = [99,98,79,60]

rec = dict(zip(name,num))                   #we can also convert a zip into a dictionary

print(rec)                                  

[print(l,k,j) for l,k,j in zip(x,y,z)]      #we can also use list comprehension
'''

# issue you might face when you were using bad practices

[print(x,y,z) for x,y,z in zip(x,y,z)]      

print(x)                                    #at this time the value of list x doesn't get affected due to list comprehension


for x,y,z in zip(x,y,z):
    print(x,y,z)
print(x)                                    #but here when we use normal for loop then the value of originals get changed