def riffle(items, out: bool = True):
    """
    Given a list of items whose length is guaranteed to be even create and 
    return a list performing a perfect riffle shuffle.
    """
    print(f"items = {items}, out={out}")
    size = len(items)
    assert(len(items) % 2 == 0)
    
    return [items[i//2] if (i % 2 == 0) == out else items[i // 2 + size//2] for i in range(size)]

print(riffle([1, 2, 3, 4, 5, 6, 7, 8]))
print(riffle([1, 2, 3, 4, 5, 6, 7, 8], out=False))
print(riffle([]))
print(riffle([], out=False))
print(riffle(['bob', 'jack']))
print(riffle(['bob', 'jack'], out=False))
