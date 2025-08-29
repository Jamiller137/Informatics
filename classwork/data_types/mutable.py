l = [1, 3, 6, 9]

print(id(l))

l.append(5)

print(id(l))


# Mutable since the location in memory does not change when the data is changed.

# Mutable data can give you problems since if you are storing data and change it then other programs
# which rely on some assumptions will still be able to call on the modified data.

# Integers, tuples, bools are immutable in that if you change the value its location in memory changes
