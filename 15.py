# Problem 15- A dictionary contains following information about 5 employees:

# First name
# Last name
# Age
# Grade(Skilled,Semi-skilled,Highly skilled)
# Write a program using map/filter/reduce  to a list of employees(first name + last name) who are highly skilled

import functools
emp=[
    {
        'first_name': 'Nishant',
        'last_name' : 'Chaurasia',
        'age' : 20,
        'grade' : 'skilled'
    },

    {
        'first_name': 'Neev',
        'last_name' : 'Thankur',
        'age' : 20,
        'grade' : 'Highly skilled'
    },

    {
        'first_name': 'Roshani',
        'last_name' : 'Rajput',
        'age' : 21,
        'grade' : 'Highly skilled'
    },

    {
        'first_name': 'Sanjana',
        'last_name' : 'Kumari',
        'age' : 20,
        'grade' : 'Semi-skilled'
    }
]


l=list(filter(lambda x:True if x['grade'].lower()=='highly skilled' else False,emp))
print(list(map(lambda x:x['first_name']+' '+x['last_name'],l)))
