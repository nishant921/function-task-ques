# write a python function that receive a list of integers and print out a histogram of binsize 10 

import math
def hist_bin(l,binsize):  
    min_bin = math.floor(min(l)/10)*10
    max_bin = math.ceil(max(l)/10)*10
     
    d={}
    for i in range(min_bin,max_bin,binsize):
        count=0
        for j in l:
           # if i+1<=j<=i+10:
            if j in range(i+1,i+binsize+1):
                count+=1
        d[str(i+1)+'-'+str(i+binsize)]=count
    return d

l=list(map(int,input("Elements: ").split()))
bin=int(input("Bin Size"))
print(hist_bin(l,bin))