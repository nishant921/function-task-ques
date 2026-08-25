# Problem-13 Using filter() and list() functions and .lower() method filter all the vowels in a given string.


s=input("String: ")
print(list(filter(lambda x:True if x.lower() in 'aeiou' else False,s)))