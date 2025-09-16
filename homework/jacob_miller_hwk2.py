"""
Homework 2

Due Date: Friday September 26 before start of class.

Make sure to put comments this homework onwards

Points: 20 (will be converted to 10 points)

"""

"""

Question 1: (5 points)

Ask the user to input a list that has as many elements as they like made from the
numbers 1 through 5 inclusive of end points.

Store these in a variable called Score of type list with each input number stored as a string.

For example, if the user inputs 5 5 4 1 then the list Score should have
['5', '5', '4', '1'].

Now write a sequence of Python statements that produces another list called
Count that contains the number of occurrences of each number (stored as str) in
numeric order of the 5 numbers. 

For the given example, count should be [1, 0, 0, 1, 2], i.e., there is one '1',
no '2' or '3', one '4' and two '5'. 

print Count

"""

# Get input as a single strings


def get_input_score():
    s = input(
        "Please enter the score as a single number whose only digits are 1, 2, 3, 4, or 5 \n (the score 5, 1, 2 should be entered as 512) \n"
    )
    score = [i for i in s]
    print(f"Score = {score}")

    score_count = [s.count(str(i)) for i in range(1, 6)]
    print(f"Score counts = {score_count}")


get_input_score()


"""
Question 2 (5 points): Write the function findChars as described in the docstring


"""


def findChars():
    """
    This function first asks the user to input a lowercase string.  It then checks the index
    position of each character in the string in an ordered list of lowercase letters (a, b, c, ... z)
    and increments the count of characters at that position.

    It returns a list of length 26 corresponding to the ordered lowercase letters with the counts
    in each cell.

    For example, if the input string is 'apple' it returns the list

    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    indicating 1 occurrence of 'a', 1 of 'e', 1 of 'l' and 2 of 'p'

    If the user enters characters in the string that are not standard lowercase letters
    the program ignores them.

    Hint: you might want to explore the string module.

    """


"""
Question 3 (5 points): Write the function checkString as described in the docstring

"""


def checkString():
    """
    This function reads strings from the given file strings.txt.

    For each string read the function determines whether it has its vowels in
    alphabetic order (a before e before i etc.).

    Eg. bleeding is in order but bloating is not.

    The function prints answers in the following format:

        string, Yes/No.

    E.g.

        bleeding, Yes
        bloating, No


    """


"""
Question 4 (5 points). Write the function reverse_vowels as described in the docstring
"""


def reverse_vowels(st):
    """
    This function takes a string as argument and returns a new string identical to the input
    string except that the vowels appear in reverse order.

    For example, when the:

    input is 'least' the function returns 'laest'
    input is 'leeast' the function returns 'laeest'
    input is 'run' the function returns 'run'
    input is 'people' the function returns 'people'

    """
