'''
test harness for hwk6
'''

import hwk6_2025_sol as std

def run_test(test_func, test_number):
    try:
        test_func()
        print(f"{test_number}: [OK]")
        print("="*100)
    except AssertionError as e:
        print(f"{test_number}: Failed ({e})")
    except Exception as e:
        print(f"{test_number}: Failed ({e})")

 
def test_readData():
    std.readData()

    expected = {'days': 3, 'onshore': 'not free', 'airline': 'included', 'liners': ['Oceana', 'Marella']}
    result = std.cruises['Greek Islands'] 
    assert(std.cruises['Greek Islands'] == expected), f"expected {expected} but got {result}"
    
def test_selectRegions():
    result = std.selectRegions('not free', 'not included')
    expected = ['Europe']
    assert(result == expected), f"expected {expected} but got {result}"

def test_totalDays():
    result = std.totalDays('Viking')
    expected = 28
    assert(result == expected), f"expected {expected} but got {result}"

def test_shortestCruise():
    result = std.shortestCruise()
    expected = [ [ ['Greek Islands', 'Oceana'], ['Greek Islands', 'Marella'] ], \
                 [ ['South Africa', 'Norwegian Dawn'], ['South Africa', 'Oceana']] ]
    assert(result == expected), f"expected {expected} but got {result}"
    
if __name__ == "__main__":
    run_test(test_readData, "readData")
    run_test(test_selectRegions, "selectRegions")
    run_test(test_totalDays, "totalDays")
    run_test(test_getLiners, "getLiners")
    run_test(test_shortestCruise, "shortestCruise")
   
