# write a python function that take a list and returns a new list with unique elements of the first list

def uni_list(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    #return list(set(l))
    return l2
    
print(uni_list([1,2,2,3]))