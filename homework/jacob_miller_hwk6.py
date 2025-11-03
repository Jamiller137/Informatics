'''
Homework 6: 2025

Total: 45 points (will be converted to 15)

Due Date: November 10 before start of class

Working with dicts, creating somewhat complex data
structures from data in files.

'''

def readData():
    '''
    (15 points)

    Parameters: None.

    This function reads in data from the file "cruises.txt" and
    creates the following two dictionaries (global variables) to be named
    as specified only: cruises and liners


    cruises =
        {'Alaska': {'days': 7, 'onshore': 'free', 'airline': 'included', \
        'liners': ['Viking', 'Seneca']},
         'Antartica': {'days': 11, 'onshore': 'none', 'airline': 'not included', \
         'liners': ['Silverline', 'P&O Cruises']},

         etc.

        }


    liners =
        {'Viking': ['Alaska', 'Caribbean', 'Mediterranean'],
         'Seneca': ['Alaska'],
         'Silverline': ['Antartica'],

         etc.
         
        }
    
    Returns None

    A few notes about the format of the input file

    1. You can assume a line in the file always start with a region name and  
       it ends with a comma separated list of liner names.
       
    2. You cannot assume that the rest of the information in between
       is in any order.

    3. There may be any number of spaces around delimiters such as | and ,

    '''
     
 
     
def selectRegions(onsh, air):
    '''
    (10 points)

    Parameters:
        onsh: represents the onshore variable
        air: represents the airline variable

    The function returns a list of regions that have cruises with matching
    onshore and airline arguments.

    For example, ['Europe'] is returned when looking
    for regions where onshore equals 'not free' and airline equals
    'not included'. 

    You need to use the cruises global variable for this.
    
    Return: list of one or more strings including possibly an empty list.

    '''

 def totalDays(liner):
    '''

    Points: 10
    
    Parameter: liner name
    
    This function returns the total number of days
    taken if one were to go on all cruises offered by a given liner.
    For example, when liner is Viking this total is 7 + 7 + 14 = 28 and
    the function returns 28.
    If the liner does not exist in the dataset then you should return 0.
    
    You need to use the liners global variable for this.

    Bonus 1 point if you can do it with list comprehension

    Returns: integer
    
    '''

 
 
def shortestCruise():
    '''
    Points: 10

    This function identifies the shortest cruises in terms of the number of days.
    It returns a list of lists containing all cruises: region and liner name,
    having this shortest number of days.
    
    For the given data the answer is as follows.
    
    (Note I am indenting so that you can understand the list structure.

    [
      [ ['Greek Islands', 'Oceana'], ['Greek Islands', 'Marella'] ],
      [ ['South Africa', 'Norwegian Dawn'], ['South Africa', 'Oceana']]
    ]

    Returns: a list of lists

    Bonus 1 point if you can use list comprehension in some of the steps

    '''

   

def main():
    '''
    include a main function that calls your functions suitably
    '''

if __name__ == "__main__":
    main()
