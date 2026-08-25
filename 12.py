# Problem-12:Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
# Input:

# list1 = [1,2,3,4,5,6]
# Output:

# [1,2,9,64,625,7..]

l=list(map(int,input("Space separated Element: ").split()))
# result=[]
# for i in range(len(l)):
#     result.append(l[i]**i)
# print(result)

print(list(map(lambda x,y:x**y,l,range(len(l)))))