# Imports

'''
Question 1

Write an algebraic expression in Python to calculate each of the following:

(a) The sum of 5, -24, 16, and square root of 80. 
(b) Absolute value of product of 9 cubed and -34.
(c) The sum of integers -76 and 14 divided by 6.
(d) Tax of 12% for dinner that included items for $13.95, $16.99 and $7.45.

'''

# (a)   5 + (-24) + 16 + 80**0.5

a = 5 + (-24) + 16 + 80**0.5

'''
    Note: While python does not have sqrt in base library we can still do exponentiation.
        An alternative approach could have been to import math and use math.sqrt(80) but the question 
        said 'algebraic' so I think this is the correct answer.
'''

# (b)   ((9**3 * (-34))**2)**0.5

b = ((9**3 * (-34))**2)**0.5

'''
    Note: Similarly to above we could use python's built-in abs function to get the same answer:
        abs(9**3 * (-34))
'''

# (c)   (-76 + 14)/6

c = (-76 + 14)/6


# (d)   0.12 * (13.95 + 16.99 + 7.45)

d = 0.12 * (13.95 + 16.99 + 7.45)


question1 = (a, b, c, d)

# I am making these tuples so they do not change when I print later.



'''
Question 2

Translate each of the following statements into Python Boolean expressions that
evaluate to True or False:

(a) The product of 8 and 13 is less than or equal to the remainder of 6000 divided
by 163.
(b) The result of 2 squared minus 3 cubed is equal to the product of 1 and -5.
(c) 2004 divided by 9 gives no remainder.
(d) 7005 divided by 5 is odd
'''

# (a)   (8 * 13 <= 6000%163) 

a = (8 * 13 <= 6000%163) 


# (b)   (2**2 - 3**3 == 1*(-5))

b = (2**2 - 3**3 == 1*(-5))


# (c)   (2004%9 == 0)

c = (2004%9 == 0)


# (d)   ((7005 // 5)%2 == 1)
"""
Use integer division because otherwise the output would be 1.0 instead of 1.
It still works with / but should be careful...
"""
d = ((7005 // 5)%2 == 1)


question2 = (a, b, c, d)



'''
Question 3

Write a function called two_numbers that asks the user to enter two numbers.  
The function then prints out the larger of the two numbers with a suitable message.
'''

def two_numbers():
    print("------------")
    print("Implementing Problem 3: Two numbers....")
    print("------------")
    try:
        num1 = float(input("Please enter the first number..."))
        num2 = float(input("Please enter the second number..."))
        numbers = [num1, num2]
        print(f"---> The largest number provided is: {max(numbers)}")
    except:
        print("ERROR: The input must be a number!")
        two_numbers()


''' 
Question 4
Write a 'single' python expression that returns the compound interest 
on a principle amount of $145000 after a duration of 5 years with the annual
rate of interest equal to 7%. Note I am asking for the interest and not the
future value of the principle.

See the following link if needed for computing compound interest.
#https://ca.indeed.com/career-advice/career-development/compound-interest-calculation


Your answers should be printed with 2 digit precision.

'''
# Answer: round(145000 * (1 + 7 / 100)**5 - 145000, 2)

def compute_compound_interest(principle: float = 145000, years: int = 5, rate: float = 7):
    """
    Parameters
    ----------
    principle: float
        The initial amount deposited.
    years: int
        The number of years the money is in the account.
    rate: float
        The percent interest for the account.
    """
    
    interest = principle * (1 + rate / 100)**years - principle
    return round(interest, 2)
    
question4 = (compute_compound_interest(),)




'''
Question 5

A ladder of length L leans against a wall and is at a distance D from the wall.
Write a function called find_height that asks the user to input the length L
and distance D and the prints the height of the wall from the ground to the point
where the ladder touches the wall.  You can assume that the dimensions are given in
feet and also print the answer in feet with a suitable message.

Your answers should be printed with 2 digit precision. 

'''

def find_height():
    """We assume that the wall makes a 90 degree angle with the floor."""

    print("------------")
    print("Implementing Problem 5: Ladder against a wall....")
    print("------------")
    try:
        length = float(input("What is the length of the ladder?"))
        distance = float(input("What is the distance from the end of the latter to the wall?"))

        height = (length**2 - distance**2)**0.5
        print(f"---> The ladder height against the wall is {round(height, 2)} ft.")
    except:
        print("ERROR: Must enter numbers where length >= distance.")
        find_height()

    



'''
Here is a function to print my answers when the homework script is ran.
'''

def print_answers(q_number: str, q_answer: tuple):
    print("-----------")
    print(f"Question {q_number}:")
    for i in range(len(q_answer)):
        print(f"({chr(97+i)}) Answer: {q_answer[i]}")

    print("-----------")


answer_list = [question1, question2, question4]

if __name__ == '__main__':
    print_answers("1", answer_list[0])
    print_answers("2", answer_list[1])
    two_numbers()
    print_answers("4", answer_list[2])
    find_height()
