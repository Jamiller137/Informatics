'''
Homework 3, 2025

Due Date: October 8, 2025

Important note: when you return a string it should be formatted exactly as required.
Differences in format - e.g., extra spaces - will fail our automated test harness.

Points:  20 (will be converted to 10 points)
'''

'''
Problem 1) There are 3 parts to question 1 below. The docstrings describe the function
to be coded.The aim is to learn about while, for and while true loops.

'''

def getFor(n: int, words: list[str]): 
    
    '''
    1a) 3 points
    
    parameters
    
        n: an integer
        words: a list of words each represented as a string

    output:

        string

    Description: 


        The function (must be built using a for loop) takes in an integer as
        parameter and list of words and returns a string.
        
        The composition of the string returned depends on the integer parameter and the wordList

        wordList = ['hello', 'brightness', 'my', 'old', 'friend', 'happy', 'to', 'see', 'you', 'again']

        Observe the examples carefully as to format of the output string.

    For example,

    getFor(4, ['hello', 'brightness', 'my', 'old', 'friend', 'happy'])
    returns
    
    'hello * brightness ** my *** old'

    getFor(5, ['hello', 'brightness', 'my', 'old', 'friend', 'happy'])
    returns

    'hello * brightness ** my *** old **** friend'

    Edge cases:

    if n < = 0 the function returns 'sorry you get an empty string'
    if n > number of words in wordList then it returns 'sorry there are not enough words'

    Makr sure you don't put extra spaces in the output or make any other changes.

    You have to use a for loop for this function.
    
    '''

    if n <= 0:
        return 'sorry you get an empty string'
    if n > len(words):
        return 'sorry there are not enough words'

    # initialize output to the first word
    output = words[0]
    
    for i in range(1, n):
        # build output star count from for loop variable
        output += ' ' + '*' * i + ' '
        output += words[i]
    return output



def getWhile(n: int, words: list[str]):
    '''
    1b) 3 points
    
    This is the same problem as in 1a, but you have to use a while loop (not a while True loop)
    '''
    if n <= 0:
        return 'sorry you get an empty string'
    if n > len(words):
        return 'sorry there are not enough words'

    # initialize output the same but now introduce a count for the while loop instead of i


    output = words[0]
    count = 1

    # we could also use words.pop(0) and make it use     while words:
    while count < n:
        output += ' ' + '*' * count + ' '
        output += words[count]
        count += 1
    return output
        





def getWhileTrue(n: int, words: list[str]):
    '''
    1c) 3 points

    This is the same problem as in 1a, but you have to use a while True loop
    
    '''
    if n <= 0:
        return 'sorry you get an empty string'
    if n > len(words):
        return 'sorry there are not enough words'
    
    # since lists are mutable using a copy of words to avoid test harness issues.
    dummy_words = words.copy()

    # cuts the while true loop
    cutoff = len(words) - n

    # initialize to first word
    output = dummy_words.pop(0)

    # star string which will get larger during the loop
    stars = '*'

    # I could just use a counter again but that's no fun
    while True:
        if len(dummy_words) <= cutoff:
            break
        output += ' ' + stars + ' '
        output += dummy_words.pop(0)
        
        stars += '*'
    return output


        


# Problem 2. Write the function twoVowels as described in its docstring

def twoVowels(st: str):
    '''
    (4 points)
    
    Parameter: st, an input string of length > 0

    Returns: A Boolean value

    This function returns True if the parameter string has only 2
    distinct vowels with each occuring only once. It returns
    False in all other cases. The function ignores case differences.

    E.g.    twoVowels('syndrome') 	        returns True.

            twoVowels('fad') 		returns False.
            
            twoVowels('parAgraph') 	returns False.
            twoVowels('bxxaAce')             returns False


    '''
    # initialize
    vowels = 'aeiou'
    
    # create vowel count list using lower for proer counting
    vowel_count = [st.lower().count(i) for i in vowels]

    # this is equivalent to exactly two disting vowels
    if max(vowel_count)==1 and sum(vowel_count)==2:
        return True

    return False

 

'''
# Problem 3. 

(7 points)

    Write a function called listCompare that takes in two lists of integers as
    arguments.
    Assign the longer list to a variable called gauge and the other list
    to a variable called inlist. If the two lists are of equal length then
    the list in the first argument is assigned to gauge and the other to inlist.

    The function compares each element of inlist
    with the elements of gauge.  If an element is greater than more than half of the
    elements of gauge then it is added to a new list called outlist.  Otherwise,
    the element is discarded. Note that if gauge is of odd length then round up
    the value that is its size divided by 2.
    So, half of the elements of gauge when it is of length 5 is 3.
    You can explore math.ceil function for this. Notice the difference
    between round and math.ceil.  Try these on 4.5 and 3.5

    The function returns outlist.

    Also when different boundary cases (e.g. empty input list/s) arise
    return the message 'Problem in your input lists'

    E.g.,

    a = [3,4,1,2]
    b = [3,1,8,9]

    listCompare2(a,b) returns [8,9]
    listCompare2(b,a) returns []

    a = [3, 4, 1, 2, 7]
    b = [3, 1, 8, 9]
    
    listCompare2(a,b) returns [8, 9]
    listCompare2(b,a) returns [8, 9]

    a = []
    b = [5,6,7]
    listCompare2(a,b) should return 'Problem in your input lists'

    Additionally, write the docstring for the listCompare function

'''

# attempting to use NumPy standard
# https://numpydoc.readthedocs.io/en/latest/format.html

def listCompare(L1: list[int], L2: list[int]):
    '''
    Description
    -----------
    Takes as input two lists of integers and outputs a list of integers.
    Picks the larger of the two input lists to be gauge while the smaller is inlist.
    If the lists have the same length then the first list is set to gauge.
    If an element x in inlist is greater than more than half of the elements in gauge then x is added to the output list.


    Notes
    -----
    Note that if gauge is of odd length then we round up (e.g. if gauge = [1, 2, 3] then every element of the output list must be > 2).


    Parameters
    ----------
    L1, L2 : list[int]
        Input lists for comparison. 


    Returns
    -------
    outlist : list[int]
    err_msg : str or None
        If there is an error or empty input list we return the string
        'Problem in your input lists'

    '''

    import math

    # setup gauge and inlist

    try:
        assert(len(L1) > 0)
        assert(len(L2) > 0)

        assert(type(L1) == list)
        assert(type(L2) == list)


        if len(L1) >= len(L2):
            gauge, inlist = L1, L2
        elif len(L1) < len(L2):
            gauge, inlist = L2, L1

        outlist = []

        for x in inlist:
            # count number of elements x is greater than
            if sum(1 for g in gauge if x > g) > math.ceil(len(gauge)/2):
                outlist.append(x)
        
        return outlist

    except:
        return 'Problem in your input lists'
