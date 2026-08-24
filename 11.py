# Problem 11: Write a Python program to add three given lists using Python map and lambda.

l=[1,2,3]
l2=[4,5,6]
l3=[7,8,9,10]

list_add=list(map(lambda x,y,z:x+y+z,l,l2,l3))
print(list_add)