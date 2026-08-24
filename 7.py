#  write a python function that accept a string as input and returns the word with the most occurrence

def most_occ(s):
    d={}
   
    for i in s.split():
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    max_val = max(d.values())
    
    for i in d:
        if d[i]==max_val:
            print(i,'->',d[i])
            
        
most_occ("hello helloo nishant nishant helloo")