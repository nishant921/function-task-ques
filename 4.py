# write a python program to print the even numbers from a given list

def even_list(l):
    res=[]
    for i in l:
        if i%2==0:
            res.append(i)
    return res
    
list1=[1,2,3,4,4,9,5]
print(even_list(list1))