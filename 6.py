# write a python function to contactinate any number of dictionary to create one 

def merge_dict(*args):
    d={}
    for i in args:
        d.update(i)
    return d

dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}

print(merge_dict(dict1,dict2,dict3))