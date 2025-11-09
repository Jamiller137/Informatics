x = [x if x%2==0 else 0 for x in range(10)]
print(x)

print(tuple(x))

print(tuple((i, i+1) for i in x))
# the above is a generator expression, not list comprehension technically
