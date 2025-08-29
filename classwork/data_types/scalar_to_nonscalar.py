# is in python integers are indivisible (no inherent methods to split it up) so is scalar

# a list or string is non-scalar since you call pull apart pieces


def get_int_digits(x: int):
    for i in range(len(str(x))):
        yield int(str(x)[i])


def make_int_digit_tuple(x: int) -> tuple:
    A = list()
    for i in get_int_digits(x):
        A.append(i)
    return tuple(A)  # here we make A a tuple so it is immutable again.


print(make_int_digit_tuple(4**7))


def convert_back(A: tuple) -> int:
    x = ""
    for i in range(len(A)):
        x = x + str(A[i])

    x = int(x)
    return x


print(convert_back(make_int_digit_tuple(4**7)))
