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
        team_name = line1[0].replace('Flamingoes', 'Flamingos')
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
        if '&' in line:
            team, win_str = line.strip().split('&')
            team = team.strip().replace('Flamingoes', 'Flamingos')

            # avoid creating an entry if details do not exist.
            if team in team_info:
                # make wins list and fix Flamingoes typo
                wins = [w.replace('Flamingoes', 'Flamingos').strip() for w in win_str.strip().split(', ') if w.strip()]
                team_info[team.strip()][4] = wins

    # update DS
    global DS
    DS = list(team_info.values())

    return None


readData()

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
    with open('output.txt', 'w') as output:
        for entry in DS:
            line1 = f"The team {entry[0]} was established in {entry[1]} and is located in {entry[2]}.\n"
            line2 = f"Team members are: {', '.join(entry[3])}.\n"

            # by default make string with no won over sentence.
            line3 = f"The team has had {len(entry[4])} wins.\n"
            
            # this edge case doesnt exist in the given data but should be handled.
            if len(entry[4]) == 1:
                line3 = f"The team has had {len(entry[4])} wins. They have won over the teams {entry[4][0]}.\n"

            # if more than one win then the given structure makes sense
            if len(entry[4]) > 1:
                line3 = f"The team has had {len(entry[4])} wins. They have won over the teams {', '.join(entry[4][:-1])} and {entry[4][-1]}.\n"

            # There is some ambiguity on if this should actually exist for the last entry...
            line4 =  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
            output.write('\n'.join([line1, line2, line3, line4]))


writeDetails()

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

    global DS

    state_dict = dict()

    # could instead do address[-2:] but that would only handle abbrev.
    get_state = lambda entry: entry[2].strip().split(' ')[-1]
    # the above is effectively taking the last word in the address string.
    
    # find state_set
    for entry in DS:
        state = get_state(entry)

        # create state in dictionary
        if state not in state_dict:
            state_dict[state] = []

        state_dict[state].append(entry[0])

    # this doesn't match the sorting that the question has if that is somehow important
    return [[state, teams] for state, teams in state_dict.items()]


def gamesPlayed(team: str):
    '''
    5 points
    
    This function takes as input a team name and returns
    the total number of games played by the team and also the number of losses

    For example, Flamingos have played 2 games and lost both of them so
    return 2, 2
    '''

    # assumes that the teams only played eachother once and no draws!
    # we can make a list of tuples (Winner, Loser)
    games = []
    for entry in DS:
        for win in entry[4]:
            games.append( (entry[0], win) )
    team_games = [g for g in games if team in g]
    
    
    total_games = len(team_games)
    num_losses = sum([1 for g in team_games if g[1] == team ])

    return total_games, num_losses


    
"""
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
