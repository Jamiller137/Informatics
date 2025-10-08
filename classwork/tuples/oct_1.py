'''
Tuples Data structure:

    () vs [] is a list

    - is immutable

    - each call points to a different piece of memory.


    Lists: Homogeneous
    Tuples: Heterogenous

    -- Not a hard and fast rule

'''

x = ('john', 4, 'male')

print(x)

st = 'test'
print(id(st))
st += 'ing'

print(id(st))

def numbers(x, y, z):
    print(x, y, z)

numbers(*[1, 2, 3])




days = {'Sun': 1, 'Mon': 2, 'Tue': 3, 'Wed': 4, 'Thu': 5, 'Fri': 6, 'Sat': 7, 'rest': 8}

x = days.pop('Wed')

print(x)

for i, v in enumerate(days):
    print(i)
    print(i, v)
