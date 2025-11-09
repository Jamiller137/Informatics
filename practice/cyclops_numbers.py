import math
def is_cyclops(n:int):
    """
    Does number have an odd number of digits where the center digit is the 
    only 0 in the number?
    """
    st = str(n)
    num_dig = len(st)

    return (num_dig % 2 == 1) and (st[math.ceil(num_dig / 2) - 1] == '0') and (sum([1 if i=='0' else 0 for i in st])==1)


test_numbers = [0, 1, 101, 98053, 777888999, 1056, 675409820] 

for x in test_numbers:
    print(x, is_cyclops(x))
