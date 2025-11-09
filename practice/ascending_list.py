def is_ascending(items: list):
    """
    Determine whether the sequence of items is strictly ascending.
    """
    print(items)
    if not items: return True

    for i in range(len(items) - 1):
        if items[i+1] - items[i] <= 0:
            return False

    return True

print(is_ascending([]))
print(is_ascending([-5, 10, 99, 123456]))
print(is_ascending([2, 3, 3, 4, 5]))
print(is_ascending([-99]))
print(is_ascending([4, 5, 6, 7, 3, 7, 9]))
