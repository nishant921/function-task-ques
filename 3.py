# write a python function that accepts a string and calculate the number of uppercase and lowercase letters 

def upper_lower(s):
    l_count=0
    u_count=0
    for i in s:
        if i.islower():
            l_count+=1
        elif i.isupper():
            u_count+=1
        else:
            pass
    return l_count,u_count
    
s=input('String: ')
l,u=upper_lower(s)
print('No.of lowercase character: ',l)
print('No.of Uppercase character: ',u) 