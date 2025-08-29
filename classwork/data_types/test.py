C = 6 + 2j

print(type(C))

print(C.real)

print(C.imag)

j = "2"

C = 6 + 1j

print(type(C))

"""e is exponentiation"""

x = 0.1 + 0.1 + 0.1
print(float.as_integer_ratio(x))
print(float.as_integer_ratio(round(0.3, 2)))

# Conclusion: Should probably default to using NumPy or SciPy

print(type(x))
print(type(x))
print(round(x, 2))
print(x)
print(type(round(0.3, 2)))

print(round(x, 2) == 0.3)
