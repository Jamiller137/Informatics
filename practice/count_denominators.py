def count_denominators(items: list[int]):
    """
    An element in a list of items is a dominator if every element to its right (not just the one element
immediately to its right, but all of them) is strictly smaller than that element. Note how according to
this de5inition, the last item of the list is automatically a dominator, regardless of its value. This func-
tion should return the count of how many elements in items are dominators. For example, the
dominators of the list [42, 7, 12, 9, 13, 5] would be 42, 13 and 5. Regardless of its value,
the last element of the list is trivially a dominator, since nothing greater follows it in the list.
Before starting to write code for this function, you should consult the parable of “Shlemiel the
painter” and think how this seemingly silly tale from a simpler time relates to today’s computational
problems performed on lists, strings and other sequences. This problem will be the 5irst of many
that you will encounter during and after this course to illustrate the important principle of using
only one loop to achieve in a tiny fraction of time the same end result that Shlemiel achieves with
two nested loops. Your workload therefore increases only linearly with respect to the number of
items, whereas the total time of Shlemiel’s back-and-forth grows quadratically, that is, as a func-
tion of the square of the number of items.
Trying to hide the inner loop of some Shlemiel algorithm inside a function call (this includes Python
built-ins such as max and list slicing) and pretending that this somehow makes those inner loops
take a constant time will only summon the Gods of Compubook Headings to return with tumult to
claim their lion’s share of execution time.
    """

    if len(items) == 0:
        return 0

    denom_count = 0
    curr_max = items[-1] - 1
    for i in range(len(items)-1, -1, -1):
        if items[i] > curr_max:
            denom_count += 1
            curr_max = max(items[i], curr_max)

    return denom_count


lists = [[42, 7, 12, 9, 2, 5], [], [-2, 5, -1, -3], [-10, -20, -30, -42], [42, 42, 42, 42], range(10**7), range(10**7, 0, -1)]

for x in lists:
    print(x)
    print(count_denominators(x))

