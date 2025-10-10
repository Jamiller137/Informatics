'''
Homework 4


Total points 40 (will be converted to 15 points)

Due Date: October 17, 2025, before start of class

To give you experience with lists, global/local variables,
functions, writing full programs, calling functions in different places
of the program etc.

You are given two input files 'teamDetails.txt' that has information about teams in some sport.
Each team has 4 players. The file format is as follows. Note there are two lines of
information for each team.

Line 1: Team name, year established, Address
Line 2: Team member names separated by comma.  There is information in asterisk that is
not used in the problem.

The second file is teamWins.txt.  It describes the wins eadh team has and is formatted as
follows:

Team name & comma separated list of teams against which the team has won.
So the first line indicates that team Parrots won against Alligators, Otters and Habaneros.

Include a main function as described in class.

'''

DS = list()  # this is a global variable. leave as is.

def readData():
    '''
    10 points
    
    This function creates reads the two input files and populates the
    global variable DS.
    
    Note the name of the global variable must be DS.

    DS has the following structure.  Essentially you have a nested list for each team.
    

    DS = 
    [
    [Team name, date, address, [Player 1 name, Player 2 name, etc.], [Team name, Team name, …] ],
    [Team name, date, address, [Player 1 name, Player 2 name, etc.], [Team name, Team name, …] ]
,

    etc.
    ]

    More generally, this structure corresponds to:

    [
    [Team name, date established, address, \
    [list of player names], [list of teams against which this team has won]
    ]
    
    next team's list
    etc
    
    ]
    
    DS is a global variable that is used by other functions as needed.

    returns None
    
    '''

    detail_file = open(file='teamDetails.txt', mode='r')
    detail_lines = detail_file.readlines()
    detail_file.close()

    # using a dict for better organization
    team_info = dict()

    for i in range(0, len(detail_lines), 2):
        # first line is team, year, and address (with commas)
        line1 = detail_lines[i].strip().split(', ')
        team_name = line1[0]
        year = line1[1]

        # line1[2:] is taking everying in the second index onwards
        # we are then joining this with a comma after the fact.
        address = ', '.join(line1[2:])

        # second line is player names
        line2 = detail_lines[i+1].strip()

        # there are some asterists in the form [*^n] to remove 
            # but we can just split along [ and take the first entry
        players = [plr.split('[')[0].strip() for plr in line2.split(', ')]
        
        # create dict entry with intial empty list for wins
        team_info[team_name] = [team_name, year, address, players, []]

    # now we get team wins 
    wins_file = open('teamWins.txt', 'r')
    win_lines = [line.strip() for line in wins_file.readlines()]
    wins_file.close()

    for line in win_lines:
        # get team and their wins
        # NOTE: This assumes that '&' is in each line
        team, win_str = line.split('&')

        # make win list
        team_wins = win_str.strip().split(', ')
        
        # if no wins leave as an empty list instead of ['']
        if team_wins[0].strip():
            team_info[team.strip()][4] = team_wins

    # update DS
    global DS
    DS = list(team_info.values())

    return None


readData()

"""
def writeDetails():
    
    '''
    5 points
    
    This function writes out to the text file called output.txt the details for
    each team in the following format:

    The team Parrots was established in 2013 and is located in 1600 Peak of the Hill, MN.

    Team members are: Garcia, Jannes, Castelle, Plunk.

    The team has had 3 wins. They have won over the teams Alligators, Otters and Habaneros.

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    The team Bonobos was established in ...... etc.

    etc.
        
    '''
 

def stateTeams():
    '''
    10 points
    
    This function returns a list with the following structure based on where
    each team is located

    [
    [state, [team name, team name, ....]],
    [state, [team name, team name ....]],
    etc.
    ]

    For example:

    [
    [MN, [Parrots, Flamingos]],
    [NY, [Habaneros]],
    etc.
    ]
    

    '''

def gamesPlayed():
    '''
    5 points
    
    This function takes as input a team name and returns
    the total number of games played by the team and also the number of losses

    For example, Flamingos have played 2 games and lost both of them so
    return 2, 2
    '''
    
def mostLosses():
    '''
    5 points
    
    This function returns a list of teams that have the most losses.
    
    '''

    
def sortByNumWins():
    '''
    5 points
    
    This function returns DS2 which is identical in
    structure to DS except that it's records are sorted in increasing
    order by number of wins.

    Hint: use a lambda function
    
    '''

    
def main():
    '''
    5 points
    
    call your functions here in a logical order
    e.g., read the data, then write it, then run the function to
    determine teams for each state etc. so you run each of your functions.
    

          

if __name__ == "__main__":
    main()


"""
