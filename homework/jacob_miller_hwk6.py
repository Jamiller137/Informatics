'''
Homework 6: 2025

Total: 45 points (will be converted to 15)

Due Date: November 10 before start of class

Working with dicts, creating somewhat complex data
structures from data in files.

'''

def readData() -> None:
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
    global cruises, liners
    cruises = {}
    liners = {}

    with open(file="cruises.txt", mode='r') as file:
        lines = file.readlines()

        # CRUISES
        for line in lines:
            # first split along |
            entry = [x.strip() for x in line.split('|')]
            # get region
            region = entry.pop(0)
            # get liners
            entry_liners = [x.strip() for x in entry.pop(-1).split(',')]

            # now entry contains just entrys for the region's dictionary
            # which we prep here:
            cruises[region] = {}
            cruises[region]['liners'] = entry_liners

            # update region's dictionary entry:
            for e in entry:
                key = e.split('=')[0].strip()
                value = e.split('=')[-1].strip()
                # make days an integer instead of a string
                if key == 'days':
                    value = int(value)

                cruises[region][key] = value
            



        # LINERS
        liner_set = set()
        for value in cruises.values():
            liner_set.update(value['liners'])

        for l in liner_set:
            # get regions which contain the liner from cruises dict
            liners[l] = [r for r in cruises.keys() if l in cruises[r]['liners']]

    return None



readData()
 
     
def selectRegions(onsh: str, air: str) -> list[str]:
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
    # this is not really necessary but I added it anyway
    global cruises

    matched_regions = []

    for key, value in cruises.items():
        if value['onshore'] == onsh and value['airline'] == air:
            matched_regions.append(key)

    return matched_regions




def totalDays(liner: str) -> int:
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
    global liners, cruises
    
    # if liner doesn't exist return 0
    if liner not in liners.keys():
        return 0

    # STEPS:
        # given liner
        # find regions where liner is included from liners dict
        # find days per region using cruises
        # sum the result

    # to write the list comprehension we go in reverse order
    return sum([ cruises[region]['days'] for region in liners[liner]])

 
 
def shortestCruise() -> list[list[list[str]]]:
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
    # STEPS:
        # find regions with the lowest days using cruises.values()
        # for each region:
            # find liners in the region using cruises[...]['liners']
            # create a list entry [region, liner]

    # to implement as a list comprehension we go in reverse order

    # here I just make it a single nested list comprehension
    # really the min days check should only be computed once
        # but it is funnier this way

    return [ [[str(region), str(liner)] \
        for liner in region_dict['liners'] ] \
        for region, region_dict in cruises.items() \
        if region_dict['days'] == min(value['days'] for value in cruises.values()) ]

   

def main():
    '''
    This demonstrates the functions from the homework. Assumes that cruises.txt is in the same directory.
    '''

    print("="*80)
    print("HOMEWORK 6: Jacob Miller")
    print("="*80)


    # readData()
    print("\n1. Loading cruise data from cruises.txt...")
    readData()

    print("\n2. Sample of loaded data:")
    print("\n   CRUISES:")
    # first 3 keys
    for region in list(cruises.keys())[:3]:
        print(f"     {region} : {cruises[region]}")

    print("\n   LINERS:")
    for liner in list(liners.keys())[:3]:
        print(f"     {liner} : {liners[liner]}")


    # selectRegions()
    print("\n" + "="*80)
    print("3. Testing selectRegions() function:")
    print("="*80)

    print("\n   Regions with onshore='not free' and airline='not included':")
    result1 = selectRegions('not free', 'not included')
    print(f"   Result: {result1}")

    print("\n   Regions with onshore='free' and airline='included':")
    result2 = selectRegions('free', 'included')
    print(f"   Result: {result2}")

    print("\n   Regions with onshore='none' and airline = 'not included':")
    result3 = selectRegions('none', 'not included')
    print(f"   Result: {result3}")


    # totalDays()
    print("\n" + "="*80)
    print("4. Testing totalDays() function:")
    print("="*80)

    test_liners = ['Viking', 'Oceana', 'Seneca', 'Iowa Cruise Liner']
    for liner in test_liners:
        days = totalDays(liner)
        regions = liners.get(liner, [])
        print(f"\n   {liner}:")
        print(f"     Regions = {regions}")
        print(f"     Total days = {days}")


    # shortestCruise()
    print("\n" + "="*80)
    print("5. Testing shortestCruise() function:")
    print("="*80)

    shortest = shortestCruise()
    min_days = min(entry['days'] for entry in cruises.values())
    print(f"\n   Shortest cruise duration: {min_days} days")
    print(f"\n   All cruises with {min_days} days:")
    for region_group in shortest:
        for cruise in region_group:
            print(f"   - Region: {cruise[0]}, Liner: {cruise[1]}")

    print("\n" + "="*80)


if __name__ == "__main__":
    main()

