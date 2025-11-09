def extract_increasing(digits:str):
    """
    Given a string of digits guaranteed to only contain ordinary integer digit characters 0 to 9, create
    and return the list of increasing integers acquired from reading these digits in order from left to
    right. The 5irst integer in the result list is made up from the 5irst digit of the string. After that, each
    element is an integer that consists of as many following consecutive digits as are needed to make
    that integer strictly larger than the previous integer. Any leftover digits at the end of the digit
    string that do not form a suf5iciently large integer are ignored.
    This problem can be solved with a for-loop through the digits that looks at each digit exactly once
    regardless of the position of that digit in the beginning, end or middle of the string. Keep track of the
    current number (initially zero) and the previous number to beat (initially equal to minus one).
    Each digit d is then processed by pinning it at the end of current number with the assignment
    current=10*current+int(d), updating the result and previous as needed.
    """
    # use .removeprefix to get rid of leading zeros
    number_list = [-1,]
    current = 0
    for d in digits:
        current = 10*current + int(d)
        if number_list[-1] < current:
            number_list.append(current)
            current = 0

    return number_list[1:]



print('1010123', extract_increasing('1010123'))
print('600005', extract_increasing('600005'))
print('045349', extract_increasing('045349'))
print('122333444455555666666', extract_increasing('122333444455555666666'))
print('1234'*100, extract_increasing('1234'*100)[-1])
