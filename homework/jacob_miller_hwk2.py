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

    print("Problem 1: \n")

    allowed_scores = ['1', '2', '3', '4', '5']

    raw_input = input(
        "Please enter the score list whose only digits are 1, 2, 3, 4, or 5 \n (the score 5, 1, 2 should be entered as 512) \n"
    )
    
    #filter for just allowed scores (makes '123' or '1 2 3' or '1, 2, 3' all work the same)
    filtered_input = "".join([c for c in raw_input if c in allowed_scores])

    Score = [i for i in filtered_input]
    print(f"Score = {Score}")

    Count = [filtered_input.count(str(i)) for i in range(1, 6)]
    print(f"Score counts = {Count}")


get_input_score()

input("\n Hit enter to proceed to the next problem...")





#################################################################################



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

    print("\n \n Problem 2: \n")

    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # could use string.ascii_lowercase to define letter list

    lower_input = input("Please input a lowercase string: \n")

    letter_count = [0 for i in range(len(letter_list))]

    for index in range(len(lower_input)):
        for letter_index in range(len(letter_list)):
            if lower_input[index] == letter_list[letter_index]:
                letter_count[letter_index] += 1
    print(letter_count)
    return letter_count

    

findChars()



def findChars_better():
    import string
    letters = string.ascii_lowercase

    lower_input = input("Please input a lowercase string: \n")

    output = []

    for c in range(len(letters)):
        output.append(lower_input.count(letters[c]))
    print(output)



input("\n Hit enter to proceed to the next problem...")




#################################################################################




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
    print("\n Problem 3: \n \n")
    
    vowels = "aeiou"
    
    # opens the strings file in the same location in read mode.
    strings_file = open('strings.txt', 'r')

    # a list of strings where each entry is a line from the file
    raw_strings = strings_file.readlines() 

    # remove line breaks and whitespace
    strings = [s.strip() for s in raw_strings]  

    for string in strings: 

        # tracks if the string is vowel-alphabetical ordered
        vowel_alphabetical = True

        latest_vowel_index = -1 # initialize at -1

        for vowel in vowels:
            # get index of vowel, returns -1 if not found
            next_vowel_index = string.find(vowel) #left most index of next vowel

            if next_vowel_index != -1: # if next vowel exists in the string 
                #check order using and so it stays false if false at any step
                vowel_alphabetical = vowel_alphabetical and (next_vowel_index > latest_vowel_index)
                # update latest non -1 vowel position
                latest_vowel_index = string.rfind(vowel) # update latest to rightmost instance of next

        # print results
        if vowel_alphabetical:
            print(f"{string}, Yes")
        else:
            print(f"{string}, No")

    strings_file.close()

checkString()

input("\n Hit enter to proceed to the next problem...")




#################################################################################



"""
Question 4 (5 points). Write the function reverse_vowels as described in the docstring
"""


def reverse_vowels(st: str):
    """
    This function takes a string as argument and returns a new string identical to the input
    string except that the vowels appear in reverse order.

    For example, when the:

    input is 'least' the function returns 'laest'
    input is 'leeast' the function returns 'laeest'
    input is 'run' the function returns 'run'
    input is 'people' the function returns 'people'

    """
    # make sure string is in lower case

    st = st.lower()
    vowels = 'aeiou'
    
    # create vowel list from st
    vowel_list = []
    for s in st:
        if s in vowels:
            vowel_list.append(s)

    # construct reversed vowel string
    st_reversed = ""
    for i in range(len(st)):
        if st[i] in vowels:
            st_reversed += vowel_list.pop()
        else:
            st_reversed += st[i]

    return st_reversed


# Output results to terminal

print("\n Problem 4: \n \n")

words = ["least", "leeast", "run", "people"]

for word in words:
    print(f"{word} --> {reverse_vowels(word)}")

input_prob_4 = input("Please input a lowercase string to test: \n")

print(f"{input_prob_4} --> {reverse_vowels(input_prob_4)}")
