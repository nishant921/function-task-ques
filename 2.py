# write a python program function that accept a hypen separated sequence of words as parameter and return the words in a hyphen separated sequence after sorting them alphabetically 

def sort_seq(s):
    temp=[]
    for i in sorted(s.split('-')):
        temp.append(i)
    return '-'.join(temp)
    #return '-'.join(sorted(s.split('-')))
    


st=input("Words: ")
print(sort_seq(st))