'''

Homework 7.  A Card Class and Game

Total 75 points (will be converted to 15 points)

Due Date: Thursday Dec 5 before start of class

Working with classes (card game with a special deck)


'''

comparison = 'simple'  # default value
Suits = ['Diamond', 'Heart', 'Spade', 'Club'] # can be changed during testing
# for example I Suits might = ['Diamond', 'Ruby', 'Amethyst', 'Gold', 'Silver']
Shapes = ['Oval', 'Square', 'Circle'] # again this too can be changed during testing
Numbers = [i for i in range(4,11)] # and this too can be changed during testing
Deck = list() # list of card instance covering all combinations of Suits, Shapes, Values
trump_suit = None  # set later randomly
trump_shape = None # set later randomly

class Card():

    '''
    
    This class defines a playing card which is different from the standard one in that
    it takes on a suit, a shape and a number.  The permissible suits, shapes and numbers
    are defined as global variables and may be changed when testing your code.
    As defined presently, there are 84 cards possible in total - one for each combination
    of suit, shape and number.

    Note: In the requirements below I use the phrase 'suitable function' or 'suitable
    method'.  You need to make the correct decision on what type of method to write
    (instance method, a class method etc.), whether to use duck typing or not for a
    method.  This decision is critical.
    
    1. Define a suitable initializer function that creates a card instance with suit,
    shape and number as input parameters. Even though cards are made automatically as
    combinations of permitted values specified in the global variables Suits, Shapes and
    Numbers you must still make sure that only legitimate arguments are provided because
    card instances may later be created by a user. Case differences must be allowed.
    For example, 'HEARTS' is the same as 'Hearts', But 'Rectangle' is not appropriate since
    it is not included in Shapes variable or 3 since it is not in Numbers variable.

        8 points
        

    2. Write a suitable method that when given a card instance X, print(X) prints out
    X's suit, shape, number as for example:
    
               This is a 'Heart-Oval-5' card

        6 points


    3. Write a suitable method is_trump_card(card, comparison). The first parameter
    represents a card instance and the second parameter comparison has the value 'simple'
    or 'complex'.  The method returns True or False based on whether the card is a trump
    card or not.  Criteria for deciding depends on whether comparison is set to 'simple'
    or 'complex'.
    
        8 points 
        

    If comparison is 'simple' then the trump is decided only on the basis of the
    suit.  If it is 'complex' it is decided both on the suit and the shape.

    Note that the trump suit and shape are set in the set_trump() method specified later.

    
    4. Write a suitable method so that given two card instances A and B, the expression
    A > B returns an appropriate integer 0,1, or 2 decided by which is the 'greater' card and
    has thus 'won' the comparison. If A has won then return 1. If B has won then return 2.
    If the cards are equal then return 0.

        8 points    

    The following is the logic for deciding which card wins.
    
    If A is a trump card and B is not trump card then A wins so return a 1.

    If B is a trump card and A is not trump card then B wins so return a 2.

    If neither is a trump card or both are trump cards then return 1 if A has the
    higher number or return 2 if B has the higher number.
    
    For all other cases it's a draw so return 0.

    Note you must use your is_trump_card function when solving for this problem.


    5. Write a suitable method called distribution(suit, shape) that returns the number
    of cards in the deck for that combination of 'suit' and 'shape' given as arguments.
    
        8 points


    In addition to the above, code for the functions specified next.
    
    '''

    # 1. init card dunder method
    def __init__(self, suit:str, shape:str, number:int):
        if suit.lower() not in [s.lower() for s in Suits]:
            raise ValueError(f"Input suit {suit} is not a valid option.")

        if shape.lower() not in [s.lower() for s in Shapes]:
            raise ValueError(f"Input shape {shape} is not a valid option.")

        if number not in Numbers:
            raise ValueError(f"Input number {number} is not a valid option.")

        self.suit = suit
        self.shape = shape
        self.number = number


    # 2. print card information
    def __str__(self) -> str:
        return f"This is a '{self.suit}-{self.shape}-{self.number}' card."

    
    def is_trump_card(self, comparison):
        pass


            

def makeDeck(): 
    '''
    No parameters
    
    The function creates a set of card instances and places
    these in a list called Deck (global variable).

    Each card is a combination of a suit, a shape and a number that are
    specified in the global variables Suits, Shapes and Numbers.
    Note their composition may change when we test the system.

    Return None

    7 points
    
    '''
    pass

    
def set_trump(): 

    '''
    No parameters
    
    This function sets the global variables trump_suit and trump_shape
    as a random choice between the possible options in the global variables
    Suits and Shapes
    
    Return None

    5 points
    
    '''
    pass
    
    
def shuffle_deck():   
    '''
    No parameters
    
    This randomly shuffles the Deck which is a global variable.
    
    Returns None

    5 points
    
    '''
    pass


def deal_one_card():  
    '''
    No parameters

    This returns the last card of the Deck. It must also remove this card from the
    Deck.

    Returns: a card instance

    5 points
    
    '''
    pass


def Game(number_rounds, compare_type): 
    '''

    15 points

    Parameters:
    
        (1) number_rounds: int > 0 specifies the number of rounds in a game. This can vary each time
        a game is played.
        
        (2) compare_type: str: 'simple' or 'complex', value for the global variable
        comparison

        This parameter is used by your Card function is_trump_card to determine
        if a card is a trump card or not. Again, possible values are 'simple' and 'complex'.

        'complex' means the trump is specified by the combination of a
        a randomly selected suit and a randomly selected shape.

        'simple' means the trump is specified only by a randomly selected suit.
    
        
    This function codes for a two player game with the Deck of cards.
    The players are referred to here as P and Q. The following are done in
    seqeunce.

    1. Set the value for the global variable comparison using the appropriate input
    argument. 2 points
    
    2. Create a Deck of cards.  The Deck has as many card instances as there are
    combinations of Suits, Shapes and Numbers (given in the global variables). 3 points

    3. Randomly select a trump suit and a trump shape and store these in the
    corresponding global variables.  3 points
    
    4.Play the game as follows.  5 points

        In each round (up to the number of rounds) the following is done:

            step 1 Deal player P a card from the Deck
            step 2 Deal player Q a card from the Deck
            step 3 Decide which player wins or if it is a draw. 
            step 4 shuffle Deck
    
        Do steps 1 through 4 number_rounds times.
        
    5. Use your distribution(suit, shape) function to get the number of trump cards with
    the trump suit and trump shape left in the deck after the game has been played.
    I refer to this number below as S.

    After the game ends, return the following data.  Pay attention to the data structure:
    
    [[Player P cards - each card in a tuple], [Player Q cards - each in a tuple], result, S]

    result is a tuple: (number of wins for P, number of wins for Q, number of draws)

    S: the result from your distribution function.
    
    For example this is what is returned in a 2 round game where I assume
    'Heart' 'Oval' is the trump combination and the comparison is set to simple.
    (note I am indenting so you can see it clearly).

    [  [('Diamond', 'Square', 4), ('Heart', 'Square', 10)],
       [('Spade', 'Circle', 9), ('Heart', 'Oval', 10)],
       (0,1,1),
       6
    ]

    '''
    pass



