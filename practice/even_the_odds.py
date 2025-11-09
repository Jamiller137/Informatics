def only_odd_digits(n:int):
    """
    Check that the given positive integer n contains only odd digits.
    """
    return all(int(d) % 2 == 1 for d in str(n))

print(5, only_odd_digits(5))
print(7531, only_odd_digits(7531))
print(482, only_odd_digits(482))
print(67, only_odd_digits(67))

