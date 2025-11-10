def group_and_skip(n:int, out:int, ins:int):
    """
    On a table there are n identical coins, to which the following operation will be applied as many
times as possible. The coins still on the table are arranged into groups of exactly out coins per
group, where out is a positive integer greater than one. For example, if n==13 and out==3, this
would use twelve of these thirteen coins to create four groups of three coins each. The n%out left-
over coins (in this example, one leftover coin) that did not make a complete group are taken aside
and recorded. After this, from each complete group, exactly ins coins are placed back on the table.
In this example, if ins==2, this will put eight coins back on the table, two coins from each of the
four groups with three coins.
Repeat this operation until the table has zero coins remaining, which will always eventually happen
whenever out>ins. Return a list that documents how many coins were taken aside in each move.
    """

    from collections import deque
    
    residue_list = []
    dummy_n = n

    while n > 0:
        dq = deque()
        while dummy_n >= out:
            dq.append(out)
            dummy_n = dummy_n - out

        residue_list.append(dummy_n)

        dummy_n = 0
        
        while dq:
            dq.pop()
            dummy_n += ins

        n = dummy_n


    return residue_list

print(group_and_skip(123456789, 10, 1))
print(group_and_skip(10**9, 13, 3))
print(group_and_skip(255, 2, 1))

# of course this is not efficient but it does model what the question asks
