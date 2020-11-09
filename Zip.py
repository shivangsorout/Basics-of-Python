x = [1,2,3,4,5,6]

y = [5,65,3,5,3,2]

z = [9,7,6,4,3,2]

for i,j in zip(x,y):
    print(i,j)

for i in zip(x,y):
    print(i)

for i,j,k in zip(x,y,z):
    print(i,j,k)



print(zip(x,y,z))               #showing that zip fuction creates a zip object