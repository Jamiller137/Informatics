'''

Homework 5: 2025

Total points 30 (will be converted to 10 points)

Homework assigned: October 17

Due Date: October 27 before start of class

Working with arrays.

'''

'''
(10 points) Problem 1: Write a function readMatrix() that reads integer data from the file "matrixdata.txt"
into an array called mymatrix in 'column dominant' format. It then returns mymatrix.

Below is an example to illustrate column dominant format.

For example, if the file has the following data:

4, 6, 9, 6, 8, 10, 14, 13, 6, 11, 16, 2

mymatrix will look on paper as follows:

    4 6 9
    6 8 10
    14 13 6
    11 16 2

mymatrix in column dominant format will look as follows:

    [[4, 6, 14, 11], [6, 8, 13, 16], [9, 10, 6, 2]]
    


You may assume that the number of integers in the input file will always
be a multiple of 4 and that you will need to make a 4 by N matrix, i.e., 4 rows and
N columns, where N varies based on the number of integers in the input file.

For example if there are 24 integers then the function generates a 4 by 6
column dominant matrix. If there are 32 integers then the matrix is 4 by 8.


Make sure to test your solution on different arrays

'''

def readMatrix():
    '''
    Description:
    ------------
    Reads a matrixdata.txt file which we assume is in the same directory
    we run the script. Then splits along `,` and will convert to a list of 
    numbers. Finally, we assume that the total numbers in the given file is 
    divisible by 4 and create and return a column dominated list of numbers.

    Returns:
    --------
    list[list[int]] : Where the inner lists are of length 4.

    Notes:
    ------
    The input file should be comma separated. We also handle input files 
    with multiple lines and treat line breaks as a new number entry. We assume 
    that the number of entries are divisible by 4. If it is not divisible by 4 
    then we truncate the remainder.

    '''

    with open(file='matrixdata.txt', mode='r') as file:
        lines = file.readlines()
        number_list = []
        
        # handle multiple lines
        for line in lines:
            # assuming , separated values on each line
            line_numbers = [int(x.strip()) for x in line.split(',') if x.strip()]
            number_list += line_numbers

        # count num_columns assuming length 4: truncates if not length 4.
        num_columns = len(number_list) // 4

        # initialize mymatrix:
        mymatrix = [ list() for i in range(num_columns)]

        # use modulus to assign entries to columns
        for index, number in enumerate(number_list):
            mymatrix[index % num_columns].append(number)

        return mymatrix

  
'''
(10 points) Problem 2: Implement a function evenRows() that takes a column dominant
array of integers (like mymatrix) and returns true if each row of the array sums up to an even
number and False otherwise (i.e., False is returned if even one row sums
to an odd number).

'''

def evenRows(mymatrix: list[list[int]]):
    '''
    Description:
    ------------
    Given an arbitrary column dominant matrix returns True if each row of the array sums 
    to an even number and False otherwise. If the input is None then we return True.

    Input:
    ------
    mymatrix = list[list[int]] : A column-dominant matrix.


    Returns:
    --------
    bool : True if each row sums to an even number and False otherwise



    '''
    # condition is trivially satisfied.
    if not mymatrix:
        return True

    num_rows = len(mymatrix[0])

    # make sure input is actually a matrix:
    if not all(len(col) == num_rows for col in mymatrix):
        raise ValueError("Invalid Matrix: Inconsistent column lengths!")

    # check sums for each row
    for row_index in range(num_rows):
        row_sum = sum(col[row_index] for col in mymatrix)

        if (row_sum % 2) != 0:
            return False

    # if we get here in the loop then all row sums are even
    return True


    

'''
(10 points) Problem 3: Write a function convert() which takes in a two dimensional
column dominant matrix
of integers (like mymatrix) and returns a transformed matrix of characters.

The transformation logic is as follows.

a) every number is replaced by its corresponding letter, e.g., 1 is a or A, 2 is b or B etc.

b) the first number of a row is always replaced by its lower case equivalent.

c) The replacement logic for the remaining numbers of a row is as follows.  If a number is
larger than ALL of the numbers to the left of it in its row then it is replaced by its
upper case letter.  If not it is replaced by its lower case letter.


So for example:

    4 6 9
    6 8 10
    14 13 6
    11 16 2


is transformed into:

    'd' 'F' 'I'
    'f' 'H' 'J'
    'n' 'm' 'f'
    'k' 'P' 'b'



'''

import copy
import string

def convert(mymatrix: list[list[int]]):
    '''
    Description:
    ------------
    Takes as an input a column-dominant matrix of integers and returns a 
    column-dominant matrix (list of lists) of letters (upper or lowercase) 
    with the same dimension. The letters corresponds to undoing a Caesar-cypher 
    on each entry. 

    For example: 
        -1 maps to 'a'/'A', 
        0 maps to 'z'/'Z', 
        1 to 'a'/'A', 
        2 to 'b'/'B', 
        ..., 
        26 to 'z'/'Z', 
        and 27 to 'a', etc.

    The character is uppercase if it is: 
        1. Not the first entry.
        2. Greater than all elements to the left of it in its row.


    Input:
    ------
    mymatrix = list[list[int]] : A column-dominant matrix.


    Returns:
    --------
    chrmatrix = list[list[int]] : A matrix with the same dimensions as mymatrix but of characters.

    '''
    
    num_rows = len(mymatrix[0])
    letters = string.ascii_lowercase

    # make sure input is actually a matrix:
    for col in mymatrix:
       assert len(col) == num_rows, f"Error: column lengths do not match."

    # initialize chrmatrix as a deep copy (since we are changing inner lists)
    # this allows using indices to iterate through the matrix
    chrmatrix = copy.deepcopy(mymatrix)

    # initialize row_maxes as the first column
    # technically this a ref not a copy: does not matter since gets reassigned
    row_maxes = mymatrix[0]

    for col_index in range(len(mymatrix)):

        #init row max list as first element.

        for row_index in range(num_rows):

            # initialize as lowercase and handle out of range integers
            # wraps for numbers > 26 while preserving comparison logic
            (chrmatrix[col_index])[row_index] = letters[((mymatrix[col_index])[row_index] - 1) % 26]

            if mymatrix[col_index][row_index] > row_maxes[row_index]:
                # convert to uppercase
                (chrmatrix[col_index])[row_index] = (chrmatrix[col_index])[row_index].upper()

        # update row maxes
        row_maxes = [max(row_maxes[i], mymatrix[col_index][i]) for i in range(num_rows)]

    return chrmatrix

