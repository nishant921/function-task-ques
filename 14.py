# Problem-14: Use reduce to convert a 2D list to 1D

import functools
# from functools import reduce

# l=[[1,2,3],[4,5,6],[7,8,9]]
n=int(input("Enter no. of list: "))
l=[]
for i in range(n):
    l.append(list(map(int,input("Element: ").split())))


print(l)
print(list(functools.reduce(lambda x,y:x+y, l)))