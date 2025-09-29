# sorting example

def distance(x):
    return abs(x-5)

# ans = sorted(x, key = distance)

# or just one line!
# ans = sorted(x, key = lambda z: abs(z-5))


n1 = [ \
        [2, 4, ['ap', 3]], \
        [9, 18, ['pot', 4]], \
        [3, 4, ['cat', 5]], \
        [1, 8, ['lady', 0]] \
        ]

# sorted(n1, key = lambda x: x[2][1])


# reduce functions

from functools import reduce

numbers = [1, 2, 3, 4]

# write any function that takes a pair of values and returns a single value of the same type.

my_add = lambda x, y: x+y

print(my_add(1, 1))
print(my_add('a', 'b'))

print(reduce(my_add, numbers))




## reduce( function, iterable)







